# HW4 ETF績效評比

## 使用的指標 Model
* ModelA. 2009_JBF_Portfolio performance evaluation with generalized Sharpe ratios_ASKSR
* ModelB. 2011_JBF_Omega performance measure and portfolio insurance
* ModelC. 2013_EL_A global index of riskiness

## ETF Data Processing

- 得到周資料與月資料
    - get_cse_week_month_data.ipynb
    - get_fe_week_month_data.ipynb
- 3篇paper的分析手法
    - ModelA: model_ASKSR.ipynb
    - ModelB: model_sharpeOmeasure.ipynb
    - ModelC: model_Riskiness.ipynb
- 分析結果：rank資料夾內做排名

### Financials Equity ETF List (51)
'FNCL', 'BDCL', 'IYG', 'BDCZ', 'IAI', 'PFI', 'KBWP', 'KBE', 'RWW',
'KCE', 'VQT', 'JHMF', 'PSP', 'QABA', 'PEX', 'KBWR', 'CHIX', 'SKF',
'KRE', 'UYG', 'KIE', 'BIZD', 'VFH', 'LBDC', 'FXO', 'RYF', 'FINZ', 'FAS',
'IAT', 'KBWD', 'EUFN', 'IXG', 'DXJF', 'LMLP', 'PHDG', 'PSCF', 'IAK',
'FAZ', 'DPST', 'KBWB', 'FINU', 'SEF', 'IYF', 'XLF', 'BDCS', 'WDRW'

### Consumer Staples Equity ETF List (26)
'XLP', 'PBJ', 'FSTA', 'EMCG', 'WBIL', 'RHS', 'KXI', 'PSL', 
'PSCC','UGE', 'IYK', 'VDC', 'WBIE', 'WBID', 'SZK', 'ECON', 'FXG'


## 分析
- 週資料或月資料結果評比相似嗎? 
    - 直接看rank內的各個csv結果，sharpe Omega差異不大，riskiness差異程度大
    - ASKSR的週資料與月資料最為相似
- 不同指標評比結果相似嗎?
    - 結果並不相同
    - 因此須針對不同目的用不同指標分析
