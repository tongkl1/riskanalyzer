from datetime import date
from dateutil.relativedelta import relativedelta
from decimal import Decimal

from data.models import BalanceSheet, IncomeSheet

def getProfitability(code : str, date : date) -> dict:
    '''
    获取公司的盈利能力信息

    Parameters:
    - code : str, 证券代码
    - date : datetime.date, 会计期间

    Return: dict<str, str> {}
    '''
    result = {'success': True}
    # 目前本函数采用动态财务值计算指标; 将来可能改成TTM方法
    # 所有涉及资产负债表与(利润表|现金流量表)交互的计算全部需要乘调整因子
    adjust_factor = Decimal('12') / Decimal(date.month)
    try:
        balance_sheet = BalanceSheet.objects.get(code=code, date=date)
        income_sheet = IncomeSheet.objects.get(code=code, date=date)
        last_balance_sheet = BalanceSheet.objects.get(code=code, date=date - relativedelta(years=1))
        last_income_sheet = IncomeSheet.objects.get(code=code, date=date - relativedelta(years=1))

        # 计算ROE及其两种分解
        # ROE = 财务杠杆 * 资产周转率 * 销售净利润率
        # ROE = 经营资产回报率 + 息差 * 净财务杠杆 = 经营净利润率 * 净经营资产周转率 + 息差 * 净财务杠杆
        net_profit = income_sheet.net_profit - max(income_sheet.non_recurrent_gain, Decimal(0))
        if balance_sheet.total_owners_equity <= 0: # 所有者权益为负, 无法计算ROE和财务杠杆
            result['roe'] = None
            result['financial_leverage'] = None
        else:
            result['roe'] = adjust_factor * net_profit / balance_sheet.total_owners_equity
            result['financial_leverage'] = balance_sheet.total_assets / balance_sheet.total_owners_equity

        # 目前还没有见到总资产为负的报表, 因此不检查分母是否非正; 下文中不做检查如无说明则理由相同
        result['asset_turnover'] = adjust_factor * income_sheet.total_revenue / balance_sheet.total_assets

        # 按比例将非经常性收益摊到营业利润包括的收益中
        # 这么做会引入一定误差, 但应该没有更好的处理方法了
        non_recurrent_gain = max(income_sheet.non_recurrent_gain * \
            (1 - (income_sheet.non_operating_income - income_sheet.non_operating_expenses) /
            (income_sheet.non_operating_income - income_sheet.non_operating_expenses + income_sheet.investment_income
            + abs(income_sheet.depreciation_expense) + abs(income_sheet.credit_devaluation_loss) +
            income_sheet.income_from_changes_in_fair_value + income_sheet.gain_on_exchange)), Decimal(0))

        nopat = (income_sheet.operating_income + income_sheet.financing_costs - non_recurrent_gain) \
            * (1 - income_sheet.income_tax_expense / income_sheet.income_before_tax)
        if income_sheet.total_revenue <= 0: # 总营业收入非正, 无法计算利润率
            result['gross_margin'] = None
            result['ros'] = None
            result['nopat_margin'] = None
            result['common_sized_income_sheet'] = None
        else:
            result['gross_margin'] = Decimal('1') - income_sheet.total_operating_cost / income_sheet.total_revenue
            result['ros'] = net_profit / income_sheet.total_revenue
            result['nopat_margin'] = nopat / income_sheet.total_revenue
            result['common_sized_income_sheet'] = {
                'revenue': Decimal('1'),
                'cogs': income_sheet.cost_of_goods_sold / income_sheet.total_revenue,
                'sg&a': (income_sheet.marketing_expenses + income_sheet.administrative_expenses) / income_sheet.total_revenue,
                'r&d': income_sheet.research_and_development_expenses / income_sheet.total_revenue,
                'finincing': income_sheet.financing_costs / income_sheet.total_revenue,
                'tax': income_sheet.income_tax_expense / income_sheet.total_revenue,
                'profit': income_sheet.net_profit / income_sheet.total_revenue
            }
            result['common_sized_income_sheet']['other'] = Decimal('2') - sum(result['common_sized_income_sheet'].values())

        working_capital = balance_sheet.total_current_assets - balance_sheet.cash_equivalent - \
            balance_sheet.loans_to_other_banks - balance_sheet.trading_assets - balance_sheet.derivative_assets - \
            balance_sheet.short_term_investment - balance_sheet.total_current_liabilities + \
            balance_sheet.short_term_borrowings + balance_sheet.loans_from_other_banks + \
            balance_sheet.held_for_trading_financial_liabilities + balance_sheet.derivative_financial_liabilities + \
            balance_sheet.non_current_liabilities_in_one_year
        net_asset = working_capital + balance_sheet.total_non_current_assets
        net_liability = net_asset - balance_sheet.total_owners_equity

        result['operating_asset_turnover'] = adjust_factor * income_sheet.total_revenue / net_asset
        result['operating_roa'] = adjust_factor * nopat / net_asset

        result['interest_rate_margin'] = result['nopat_margin'] - adjust_factor * income_sheet.financing_costs * \
            (1 - income_sheet.income_tax_expense / income_sheet.income_before_tax) / net_liability

        result['net_financial_leverage'] = net_liability / balance_sheet.total_owners_equity

        # 识别是否有大笔非经常性损益
        result['huge_non_recurrent_income'] = income_sheet.non_recurrent_gain > 0 \
            and income_sheet.net_profit < 6 * income_sheet.non_recurrent_gain
        result['turn_to_profit_by_non_recurrent_income'] = income_sheet.non_recurrent_gain > 0 \
            and income_sheet.net_profit < income_sheet.non_recurrent_gain

        # 判断洗大澡的规则比较复杂, 具体规则如下
        # 0(必须满足). 净利润为负
        # 1. 扣非净利润和非经常性损益均为负
        # 2. 管理费用、销售费用出现大幅增长
        # 3. 资产减值损失或信用减值损失大幅增加, 且应收账款、存货、长期股权投资、固定资产、商誉有至少一项大幅减少
        result['big_bath'] = income_sheet.net_profit < 0 and ((
            income_sheet.non_recurrent_gain < 0 and income_sheet.net_profit < income_sheet.non_recurrent_gain) or
            income_sheet.marketing_expenses > last_income_sheet.marketing_expenses * Decimal('1.5') or
            income_sheet.administrative_expenses > last_income_sheet.administrative_expenses * Decimal('1.5') or
            ((abs(income_sheet.depreciation_expense) > abs(last_income_sheet.depreciation_expense) * Decimal('1.5') or
            abs(income_sheet.credit_devaluation_loss) > abs(last_income_sheet.credit_devaluation_loss) * Decimal('1.5'))
            and (balance_sheet.bills_receivable + balance_sheet.accounts_receivable <
            (last_balance_sheet.bills_receivable + last_balance_sheet.accounts_receivable) * Decimal('0.5') or
            balance_sheet.inventories < last_balance_sheet.inventories * Decimal('0.5') or
            balance_sheet.long_term_equity_investment + balance_sheet.long_term_bond_investment
            + balance_sheet.long_term_investment + balance_sheet.other_equity_investment < (
            last_balance_sheet.long_term_equity_investment + last_balance_sheet.long_term_bond_investment
            + last_balance_sheet.long_term_investment + last_balance_sheet.other_equity_investment) * Decimal('0.8') or
            balance_sheet.fixed_assets < last_balance_sheet.fixed_assets * Decimal('0.8') or
            balance_sheet.construction_work_in_progress < last_balance_sheet.construction_work_in_progress * Decimal('0.7') or
            balance_sheet.goodwill < last_balance_sheet.goodwill * Decimal('0.6')
            ))
        )

        result['admin_cost_increase'] = income_sheet.administrative_expenses > \
            last_income_sheet.administrative_expenses * Decimal('1.5')

    except (BalanceSheet.DoesNotExist, IncomeSheet.DoesNotExist):
        print('Stock {} at period {} doesn\'t have at least one of the three financial statements.'.format(code, date))
        result['success'] = False

    return result
