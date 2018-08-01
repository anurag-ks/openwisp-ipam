# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import swapper
from django.contrib import admin

from openwisp_ipam.admin import AbstractIpAddressAdmin, AbstractSubnetAdmin

IpAddress = swapper.load_model("openwisp_ipam", "IpAddress")
Subnet = swapper.load_model("openwisp_ipam", "Subnet")


@admin.register(IpAddress)
class IPAddressAdmin(AbstractIpAddressAdmin):
    pass


@admin.register(Subnet)
class SubnetAdmin(AbstractSubnetAdmin):
    app_name = "sample_ipam"
