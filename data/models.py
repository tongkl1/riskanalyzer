from django.db import models

class BalanceSheet(models.Model):
    # 证券代码
    code = models.CharField(max_length=64)
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
    customer_bank_deposits_and_due_to_banks_and_other_financial_institutions = models.DecimalField(max_digits=20, decimal_places=3, default=0)
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

# class IncomeSheet(models.Model):
#     # 证券代码
#     code = models.CharField(max_length=64)
#     # 会计期间
#     date = models.DateField()
#     # 营业总收入
#     #   营业收入
#     #   利息净收入 (金融类公司)
#     #     利息收入
#     #     - 利息支出
#     #   已赚保费
#     #   保险业务收入
#     #   其中: 分保费收入
#     #     - 分出保费
#     #     - 提取未到期责任准备金
#     #   手续费及佣金净收入
#     #     其中: 代理买卖证券业务净收入
#     #     其中: 证券承销业务净收入
#     #     其中: 受托客户资产管理业务净收入
#     #     手续费及佣金收入
#     #     - 手续费及佣金支出
#     #   其他业务收入
#     # 营业总成本
#     #   营业成本
#     #   退保金
#     #   赔付支出净额
#     #   赔付支出
#     #   减: 摊回赔付支出
#     #   提取保险责任准备金净额
#     #   提取保险责任准备金
#     #   减: 摊回保险责任准备金
#     #   保单红利支出
#     #   分保费用
#     #   研发费用
#     #   营业税金及附加
#     #   业务及管理费
#     #   减: 摊回分保费用
#     #   销售费用
#     #   管理费用
#     #   财务费用
#     #     其中: 利息费用
#     #     其中: 利息收入
#     # 资产减值损失
#     # 其他业务成本
#     # 公允价值变动收益
#     # 投资收益
#     # 其中: 对联营企业和合营企业的投资收益
#     # 汇兑收益
#     # 其他业务利润
#     # 营业利润
#     # 营业外收入
#     # 其中: 非流动资产处置利得
#     # 营业外支出
#     # 其中: 非流动资产处置净损益
#     # 其中: 非流动资产处置损失
#     # 利润总额
#     # 所得税费用
#     # 未确认的投资损失
#     # 影响净利润的其他项目
#     # 净利润
#     # 归属于母公司所有者的净利润
#     # 少数股东损益
#     # 基本每股收益
#     # 稀释每股收益
#     # 其他综合收益(损失)
#     # 综合收益总额
#     # 归属于母公司所有者的综合收益
#     # 归属少数股东的综合收益
#     # 其他收益
#     # 其中: 以摊余成本计量的金融资产终止确认收益
#     # 净敞口套期收益
#     # 信用减值损失
#     # 资产处置收益
#     # 归属于母公司其他权益工具持有者的净利润

# class CashflowSheet(models.Model):
#     # 证券代码
#     code = models.CharField(max_length=64)
#     # 会计期间
#     date = models.DateField()
#     # 销售商品、提供劳务收到的现金
#     # 客户存款和同业存放款项净增加额
#     # 向中央银行借款净增加额
#     # 向其他金融机构拆入资金净增加额
#     # 收到原保险合同保费取得的现金
#     # 收到再保险业务现金净额
#     # 保户储金及投资款净增加额
#     # 处置交易性金融资产净增加额
#     # 收取利息、手续费及佣金的现金
#     # 拆入资金净增加额
#     # 回购业务资金净增加额
#     # 收到的税费返还
#     # 收到的其他与经营活动有关的现金
#     # 购买商品、接受劳务支付的现金
#     # 客户贷款及垫款净增加额
#     # 存放中央银行和同业款项净增加额
#     # 支付原保险合同赔付款项的现金
#     # 支付利息、手续费及佣金的现金
#     # 支付保单红利的现金
#     # 支付给职工以及为职工支付的现金
#     # 支付的各项税费
#     # 支付其他与经营活动有关的现金
#     # 经营活动产生的现金流量净额
#     # 收回投资收到的现金
#     # 取得投资收益收到的现金
#     # 处置固定资产、无形资产和其他长期资产收回的现金净额
#     # 处置子公司及其他营业单位收到的现金净额
#     # 收到的其他与投资活动有关的现金
#     # 购建固定资产、无形资产和其他长期资产支付的现金
#     # 投资支付的现金
#     # 质押贷款净增加额
#     # 取得子公司及其他营业单位支付的现金净额
#     # 支付其他与投资活动有关的现金
#     # 投资活动产生的现金流量净额
#     # 吸收投资收到的现金
#     # 吸收权益性投资收到的现金
#     # 其中: 子公司吸收少数股东投资收到的现金
#     # 发行债券收到的现金
#     # 取得借款收到的现金
#     # 收到其他与筹资活动有关的现金
#     # 偿还债务支付的现金
#     # 分配股利、利润或偿付利息支付的现金
#     # 其中: 子公司支付给少数股东的股利、利润
#     # 支付其他与筹资活动有关的现金
#     # 筹资活动产生的现金流量净额
#     # 汇率变动对现金及现金等价物的影响
#     # 其他对现金的影响
#     # 现金及现金等价物净增加额
#     # 期初现金及现金等价物余额
#     # 期末现金及现金等价物余额

#     # 净利润
#     # 未确认的投资损失
#     # 资产减值准备
#     # 固定资产折旧、油气资产折耗、生产性生物资产折旧
#     # 无形资产摊销
#     # 长期待摊费用摊销
#     # 处置固定资产、无形资产和其他长期资产的损失(收益以“－”号填列）
#     # 固定资产报废损失(收益以“－”号填列）
#     # 公允价值变动损失(收益以“－”号填列）
#     # 财务费用(收益以“－”号填列）
#     # 投资损失(收益以“－”号填列）
#     # 递延所得税资产减少（增加以“－”号填列）
#     # 递延所得税负债增加（减少以“－”号填列）
#     # 存货的减少（增加以“－”号填列）
#     # 经营性应收项目的减少（增加以“－”号填列）
#     # 经营性应付项目的增加（减少以“－”号填列）
#     # 其他
#     # 经营活动产生的现金流量净额
#     # 债务转为资本
#     # 一年内到期的可转换公司债券
#     # 融资租赁固定资产
#     # 现金的期末余额
#     # 现金的期初余额
#     # 现金等价物的期末余额
#     # 现金等价物的期初余额
#     # 现金及现金等价物净增加额
#     # 信用减值损失