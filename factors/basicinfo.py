from data.models import BasicInformation

def getBasicInformation(code : str) -> dict:
    '''
    获取公司的基本信息

    Parameters:
    - code : str, 证券代码

    Return: dict<str, str> {'name': 证券简称, 'price': 当前价格, 'status': 当前状态, 'industry': 所属行业}
    '''
    result = {'name': '--', 'price': '--', 'status': '--', 'industry': '--'}
    try:
        obj = BasicInformation.objects.get(pk=code)
        # 当前没有实现价格的获取, 暂时返回占位符'--'
        result['name'] = obj.name
        result['price'] = '--'
        result['status'] = dict(BasicInformation.LIST_STATUS_CHOICES)[obj.list_status]
        result['industry'] = obj.industry_name
    except BasicInformation.DoesNotExist:
        print('Stock {} has no basic information entry.'.format(code))
    return result
