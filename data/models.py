from django.db import models

class BasicInformation(models.Model):
    # 证券代码
    code = models.CharField(max_length=64, primary_key=True)
    # 证券简称
    name = models.CharField(max_length=64)
    # 公司全称
    full_name = models.CharField(max_length=256)
    # 行业代码
    industry_code = models.CharField(max_length=5)
    # 行业名称
    industry_name = models.CharField(max_length=64)
    # 上市日期
    list_date = models.DateField()

    # 交易状态
    NORMAL = 'A'
    DELISTED = 'D'
    SUSPEND_LISTING = 'S'
    SUSPEND_TRADING = 'N'

    LIST_STATUS_CHOICES = [
        (NORMAL, '正常交易'),
        (DELISTED, '终止上市'),
        (SUSPEND_LISTING, '暂停上市'),
        (SUSPEND_TRADING, '停牌'),
    ]

    list_status = models.CharField(max_length=2, choices=LIST_STATUS_CHOICES, default=NORMAL)

    def __str__(self):
       return self.code + " " + self.name

class BalanceSheet(models.Model):
    # 证券代码
    code = models.CharField(max_length=64, db_index=True)
    # 会计期间
    date = models.DateField()
    # 货币资金
    cash_equivalent = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中:客户资金存款
    client_deposit = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 结算备付金
    balances_with_clearing_companies = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中: 客户备付金
    balances_with_client = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 现金及存放中央银行款项
    cash_bank = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 存放同业款项
    deposits_in_other_bank = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 贵金属
    noble_metal = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 拆出资金
    loans_to_other_banks = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 交易性金融资产
    trading_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 衍生金融资产
    derivative_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 短期投资
    short_term_investment = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应收票据
    bills_receivable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应收账款
    accounts_receivable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应收款项融资
    accounts_receivable_financing = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 预付款项
    advance_payment = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应收保费
    insurance_receivable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应收分保账款
    reinsurance_receivable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应收代位追偿款
    subrogation_receivables = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应收分保合同准备金
    reinsurance_contract_reserves_receivable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应收利息
    interest_receivable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应收股利
    dividend_receivable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他应收款
    other_receivable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 买入返售金融资产
    bought_sellback_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 存货
    inventories = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 合同资产
    contract_asset = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 一年内到期的非流动资产
    non_current_asset_in_one_year = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 存出保证金
    refundable_deposits = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他流动资产
    other_current_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 流动资产合计
    total_current_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 保户质押贷款
    policy_pledge_loans = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 定期存款
    time_deposit = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 发放贷款及垫款
    loans_and_advances_to_customers = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 可供出售金融资产
    available_for_sale_financial_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 持有至到期投资
    held_to_maturity_investments = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 债权投资
    bond_investment = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他债权投资
    other_bond_investment = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 长期应收款
    long_term_receivables = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 长期股权投资
    long_term_equity_investment = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 长期债权投资
    long_term_bond_investment = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 长期投资
    long_term_investment = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他权益工具投资
    other_equity_investment = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他非流动金融资产
    other_noncurrent_asset = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 存出资本保证金
    statutory_deposits = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 独立账户资产
    seperate_account_asset = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 投资性房地产
    investment_properties = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 固定资产
    fixed_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 在建工程
    construction_work_in_progress = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 工程物资
    construction_materials = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 固定资产清理
    fixed_assets_pending_for_disposal = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 生产性生物资产
    bearer_biological_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 油气资产
    oil_and_gas_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 无形资产
    intangible_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中: 交易席位费
    transaction_seat_fees = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 开发支出
    development_cost = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 商誉
    goodwill = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 长期待摊费用
    long_term_prepaid_expenses = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 递延所得税资产
    deferred_tax_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他非流动资产
    other_non_current_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 非流动资产合计
    total_non_current_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他资产
    other_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 资产总计
    total_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 短期借款
    short_term_borrowings = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中:质押借款
    pledge_loan = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 向中央银行借款
    borrowings_from_central_bank = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 吸收存款及同业存放
    customer_bank_deposits_and_due_to_banks = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中: 同业及其他金融机构存放款项
    due_to_banks_and_other_financial_institutions = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中: 吸收存款
    customer_bank_deposits = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 拆入资金
    loans_from_other_banks = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 交易性金融负债
    held_for_trading_financial_liabilities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 衍生金融负债
    derivative_financial_liabilities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应付票据
    notes_payable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应付账款
    accounts_payable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 预收款项
    advance_receipts = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 合同负债
    contract_liability = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 卖出回购金融资产款
    funds_from_repurchasing_financial_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应付手续费及佣金
    charges_and_commission_payable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应付职工薪酬
    staff_remuneration_payables = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应交税费
    tax_payable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应付利息
    interest_payable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应付股利
    dividend_payable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应付赔付款
    indemnity_accounts_payable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应付保单红利
    policyholder_dividend_payable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 保户储金及投资款
    deposits_from_policyholders = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 保险合同准备金
    insurance_contract_reserves = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他应付款
    other_payables = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应付分保账款
    reinsured_accounts_payable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 代理买卖证券款
    funds_from_securities_trading_agency = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 代理承销证券款
    funds_from_underwriting_securities_agency = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 预收保费
    premiums_received_in_advance = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 一年内到期的非流动负债
    non_current_liabilities_in_one_year = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他流动负债
    other_current_liabilities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 流动负债合计
    total_current_liabilities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 长期借款
    long_term_borrowings = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 独立账户负债
    separate_account_liabilities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 应付债券
    bonds_payable = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 长期应付款
    long_term_payables = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 专项应付款
    special_payables = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 长期负债合计
    total_long_term_liabilities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 预计负债
    estimated_liabilities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 递延所得税负债
    deferred_income_tax_liabilities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他非流动负债
    other_non_current_liabilities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 递延收益
    deferred_revenue = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 非流动负债合计
    total_non_current_liabilities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他负债
    other_liabilities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 负债合计
    total_liabilities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 实收资本(或股本)
    paid_in_capital = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他权益工具
    other_equity_instruments = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中: 优先股
    preferred_stocks = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中: 永续债
    perpetual_bonds = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中: 其他
    other_equity_instruments_other = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 资本公积
    capital_reserves = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中: 库存股
    treasury_stock = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 盈余公积
    surplus_reserves = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 一般风险准备
    general_risk_provisions = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 未分配利润
    retained_earnings = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 外币报表折算差额
    foreign_currency_translation_differences = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 未确认的投资损失
    unrealized_investment_losses = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 交易风险准备
    trading_risk_provisions = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 专项储备
    special_reserves = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他综合收益
    other_comprehensive_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 归属于母公司所有者权益合计
    total_equity_attributable_to_equity_holders = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 少数股东权益
    minority_interests = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 所有者权益合计
    total_owners_equity = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 负债与所有者权益总计
    total_liabilities_and_owners_equity = models.DecimalField(max_digits=20, decimal_places=3, default=0)

    def __str__(self):
        return self.code + "@" + str(self.date)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=("code", "date"), name="balance_sheet_unique_code_date")
        ]

class IncomeSheet(models.Model):
    # 证券代码
    code = models.CharField(max_length=64, db_index=True)
    # 会计期间
    date = models.DateField()
    # 营业总收入
    total_revenue = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   营业收入
    operating_revenue = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   利息净收入 (金融类公司)
    net_interest_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #     利息收入
    interest_income_fin = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #     - 利息支出
    interest_expenses_fin = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   已赚保费
    earned_premium = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   保险业务收入
    income_from_insurance_business = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   其中: 分保费收入
    reinsurance_premium_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #     - 分出保费
    reinsurance_premium_ceded = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #     - 提取未到期责任准备金
    appropriation_of_deposit_for_undue_duty = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   手续费及佣金净收入
    net_fee_and_commission_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #     其中: 代理买卖证券业务净收入
    net_securities_trading_agency_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #     其中: 证券承销业务净收入
    net_securities_underwriting_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #     其中: 受托客户资产管理业务净收入
    net_trusted_customer_asset_management_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #     手续费及佣金收入
    fee_and_commission_revenue = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #     - 手续费及佣金支出
    fee_and_commission_expenses = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   其他业务收入
    other_operating_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 营业总成本
    total_operating_cost = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   营业成本
    cost_of_goods_sold = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   退保金
    refunded_premiums = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   赔付支出净额
    net_claims_paid = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   赔付支出
    claims_paid = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   减: 摊回赔付支出
    reinsurers_share_of_claims_paid = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   提取保险责任准备金净额
    net_appropriation_of_deposit_for_duty = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   提取保险责任准备金
    appropriation_of_deposit_for_duty = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   减: 摊回保险责任准备金
    amortized_appropriation_of_deposit_for_duty = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   保单红利支出
    policyholder_dividend_expense = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   分保费用
    reinsurance_expenses = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   研发费用
    research_and_development_expenses = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   营业税金及附加
    sales_tax_and_extra_charges = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   业务及管理费
    sales_and_management_expenses = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   减: 摊回分保费用
    refund_of_reinsurance_premium_ceded = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   销售费用
    marketing_expenses = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   管理费用
    administrative_expenses = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #   财务费用
    financing_costs = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #     其中: 利息费用
    interest_expenses = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    #     其中: 利息收入
    interest_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 资产减值损失
    depreciation_expense = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他业务成本
    cost_of_other_operations = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 公允价值变动收益
    income_from_changes_in_fair_value = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 投资收益
    investment_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 汇兑收益
    gain_on_exchange = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他业务利润
    income_from_other_operations = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 营业利润
    operating_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 营业外收入
    non_operating_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中: 非流动资产处置利得
    gain_from_disposal_of_non_current_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 营业外支出
    non_operating_expenses = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中: 非流动资产处置净损益
    net_gain_from_disposal_of_non_current_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中: 非流动资产处置损失
    loss_from_disposal_of_non_current_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 利润总额
    income_before_tax = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 所得税费用
    income_tax_expense = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 未确认的投资损失
    unrealized_investment_loss = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 影响净利润的其他项目
    other_subjects_affecting_net_profit = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 净利润
    net_profit = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 归属于母公司所有者的净利润
    net_income_attributable_to_shareholders = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 非经常性损益
    non_recurrent_gain = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 归属于母公司所有者的扣除非经常性损益的净利润
    net_income_less_non_recurrent_gain = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 少数股东损益
    gains_losses_attributable_to_minority_interests = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 基本每股收益
    basic_earnings_per_share = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 稀释每股收益
    diluted_earnings_per_share = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他综合收益(损失)
    other_comprehensive_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 综合收益总额
    accumulated_other_comprehensive_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 归属于母公司所有者的综合收益
    aoci_attributable_to_shareholders = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 归属少数股东的综合收益
    aoci_attributable_to_minority = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他收益
    other_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 净敞口套期收益
    net_exposure_hedging_income = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 信用减值损失
    credit_devaluation_loss = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 资产处置收益
    gain_from_non_currunt_assets_disposal = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 归属于母公司其他权益工具持有者的净利润
    net_income_to_other_equity_instruments_holder = models.DecimalField(max_digits=20, decimal_places=3, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=("code", "date"), name="income_sheet_unique_code_date")
        ]

    def __str__(self):
        return self.code + "@" + str(self.date)

class CashflowSheetDirect(models.Model):
    # 证券代码
    code = models.CharField(max_length=64, db_index=True)
    # 会计期间
    date = models.DateField()
    # 销售商品、提供劳务收到的现金
    cash_receipts_from_customers = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 客户存款和同业存放款项净增加额
    net_gains_of_customer_deposits_and_due_to_banks = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 向中央银行借款净增加额
    net_gains_of_borrowings_from_central_bank = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 向其他金融机构拆入资金净增加额
    net_gains_of_loans_from_other_banks = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 收到原保险合同保费取得的现金
    cash_from_receiving_insurance_premium = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 收到再保险业务现金净额
    net_cash_from_reinsurance_business = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 保户储金及投资款净增加额
    net_gains_of_deposits_from_policyholders = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 处置交易性金融资产净增加额
    net_gains_of_disposal_of_tradable_financial_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 收取利息、手续费及佣金的现金
    cash_received_from_interests_fees_and_commissions = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 拆入资金净增加额
    net_gains_of_loans_from_other_banks2 = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 回购业务资金净增加额
    net_gains_of_repurchase_business_capital = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 收到的税费返还
    refund_of_taxes_and_surcharges = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 收到的其他与经营活动有关的现金
    cash_received_from_other_operating_activities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 购买商品、接受劳务支付的现金
    cash_paid_for_goods_and_services = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 客户贷款及垫款净增加额
    net_gains_of_loans_and_advances_to_customers = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 存放中央银行和同业款项净增加额
    net_gains_of_deposits_in_central_bank_and_other_banks = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 支付原保险合同赔付款项的现金
    cash_paid_for_indemnity = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 支付利息、手续费及佣金的现金
    cash_paid_for_interests_fees_commissions = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 支付保单红利的现金
    cash_paid_for_policy_dividends = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 支付给职工以及为职工支付的现金
    cash_paid_to_and_on_behalf_of_employees = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 支付的各项税费
    cash_paid_for_taxes = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 支付其他与经营活动有关的现金
    cash_paid_related_to_other_operating_activities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 经营活动产生的现金流量净额
    cashflow_from_operating_activities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 收回投资收到的现金
    cash_received_from_disposal_of_investments = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 取得投资收益收到的现金
    cash_received_from_gain_of_investment_revenue = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 处置固定资产、无形资产和其他长期资产收回的现金净额
    cash_from_disposal_of_fixed_intangible_other_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 处置子公司及其他营业单位收到的现金净额
    cash_from_disposal_of_subsidiaries = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 收到的其他与投资活动有关的现金
    cash_received_related_to_other_investing_activities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 购建固定资产、无形资产和其他长期资产支付的现金
    cash_to_acquire_fixed_intangible_and_other_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 投资支付的现金
    cash_paid_to_acquire_investments = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 质押贷款净增加额
    net_gains_of_pledge_loans = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 取得子公司及其他营业单位支付的现金净额
    cash_to_acquire_subsidiaries = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 支付其他与投资活动有关的现金
    cash_paid_related_to_other_investing_activities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 投资活动产生的现金流量净额
    net_cash_flows_from_investing_activities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 吸收投资收到的现金
    cash_from_capital_contributions = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 吸收权益性投资收到的现金
    cash_from_capital_contributions_subsidiaries = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中: 子公司吸收少数股东投资收到的现金
    cash_from_capital_contributions_minority = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 发行债券收到的现金
    cash_received_from_issuing_bonds = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 取得借款收到的现金
    cash_received_from_borrowings = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 收到其他与筹资活动有关的现金
    cash_received_related_to_other_financing_activities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 偿还债务支付的现金
    cash_repayments_of_borrowings = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 分配股利、利润或偿付利息支付的现金
    cash_for_dividends_profits_or_interests = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其中: 子公司支付给少数股东的股利、利润
    cash_for_dividends_profit_to_minority_shareholders = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 支付其他与筹资活动有关的现金
    cash_related_to_other_financing_activities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 筹资活动产生的现金流量净额
    net_cash_flows_from_financing_activities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 汇率变动对现金及现金等价物的影响
    effect_of_foreign_exchange_rate_changes_on_cash = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他对现金的影响
    effect_of_other_factors_on_cash = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 现金及现金等价物净增加额
    net_gains_of_cash_and_cash_equivalents = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 期初现金及现金等价物余额
    cash_begin = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 期末现金及现金等价物余额
    cash_end = models.DecimalField(max_digits=20, decimal_places=3, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=("code", "date"), name="cashflow_sheet_unique_code_date")
        ]

    def __str__(self):
       return self.code + "@" + str(self.date)

class CashflowSheetIndirect(models.Model):
    # 证券代码
    code = models.CharField(max_length=64, db_index=True)
    # 会计期间
    date = models.DateField()
    # 净利润
    net_profit = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 信用减值损失
    credit_impairment_loss = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 未确认的投资损失
    unrealized_investment_losses = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 资产减值准备
    allocation_of_assets_impairment = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 固定资产折旧、油气资产折耗、生产性生物资产折旧
    depreciations_of_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 无形资产摊销
    amortization_of_intangibles = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 长期待摊费用摊销
    amortization_of_long_term_deferred_expenses = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 处置固定资产、无形资产和其他长期资产的损失(收益以“－”号填列）
    loss_from_disposal_of_fixed_intangible_other_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 固定资产报废损失(收益以“－”号填列）
    loss_on_disposal_of_fixed_asset = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 公允价值变动损失(收益以“－”号填列）
    loss_from_fair_value_change = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 财务费用(收益以“－”号填列）
    finance_charge = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 投资损失(收益以“－”号填列）
    investment_loss = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 递延所得税资产减少（增加以“－”号填列）
    decrease_of_deferred_tax_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 递延所得税负债增加（减少以“－”号填列）
    increase_of_deferred_tax_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 存货的减少（增加以“－”号填列）
    decrease_of_inventories = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 经营性应收项目的减少（增加以“－”号填列）
    decrease_of_receivables_in_operating = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 经营性应付项目的增加（减少以“－”号填列）
    increase_of_receivables_in_operating = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 其他
    other = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 经营活动产生的现金流量净额
    net_cash_flows_from_operating_activities = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 债务转为资本
    conversion_of_debt_into_capital = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 一年内到期的可转换公司债券
    convertible_bonds_maturing_within_one_year = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 融资租赁固定资产
    financial_leased_fixed_assets = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 现金的期末余额
    cash_end = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 现金的期初余额
    cash_begin = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 现金等价物的期末余额
    cash_equivalents_end = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 现金等价物的期初余额
    cash_equivalents_begin = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    # 现金及现金等价物净增加额
    net_gains_of_cash_and_cash_equivalents = models.DecimalField(max_digits=20, decimal_places=3, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=("code", "date"), name="cashflow_sheet_indirect_unique_code_date")
        ]

    def __str__(self):
       return self.code + "@" + str(self.date)

class ReportAudit(models.Model):
    # 证券代码
    code = models.CharField(max_length=64, db_index=True)
    # 会计期间
    date = models.DateField()

    # 审计意见类型
    UNQUALIFIED = 1
    QUALIFIED = 2
    ADVERSE = 3
    DISCLAIMER = 4
    UNQUALIFIED_WITH_NOTES = 5
    QUALIFIED_WITH_NOTES = 6
    ADVERSE_WITH_NOTES = 7
    NONE = -1

    AUDIT_TYPE_CHOICES = [
        (UNQUALIFIED, '标准无保留意见'),
        (QUALIFIED, '保留意见'),
        (ADVERSE, '否定意见'),
        (DISCLAIMER, '无法发表意见'),
        (UNQUALIFIED_WITH_NOTES, '无保留意见加事项段'),
        (QUALIFIED_WITH_NOTES, '保留意见加事项段'),
        (ADVERSE_WITH_NOTES, '否定意见加说明段'),
        (NONE, '未经审计')
    ]

    AUDIT_TYPE_MAPPING = {
        '标准无保留意见': 1,
        '保留意见': 2,
        '否定意见': 3,
        '无法发表意见': 4,
        '拒绝发表意见': 4,
        '无保留意见加事项段': 5,
        '无保留意见加说明段': 5,
        '保留意见加事项段': 6,
        '保留意见加说明段': 6,
        '否定意见加说明段': 7,
        '': -1
    }

    audit_type = models.IntegerField(choices=AUDIT_TYPE_CHOICES, default=UNQUALIFIED)

    # 审计意见
    audit_remark = models.CharField(max_length=10000, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=("code", "date"), name="report_audit_unique_code_date")
        ]

    def __str__(self):
       return self.code + "@" + str(self.date)
