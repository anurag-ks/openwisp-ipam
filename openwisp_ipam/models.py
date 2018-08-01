from swapper import swappable_setting

from django_ipam.models import AbstractIpAddress, AbstractSubnet


class Subnet(AbstractSubnet):
    class Meta(AbstractSubnet.Meta):
        abstract = False
        swappable = swappable_setting('openwisp_ipam', 'Subnet')
        app_label = 'openwisp_ipam'


class IpAddress(AbstractIpAddress):
    class Meta(AbstractIpAddress.Meta):
        abstract = False
        swappable = swappable_setting('openwisp_ipam', 'IpAddress')
        app_label = 'openwisp_ipam'
