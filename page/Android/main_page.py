# encoding: utf-8
"""
@author: 宋坤坤
@contact: cailyn.song@isysful.com
@time: 2022/6/6 17:18
@file: Navigation_Bar.py
@desc: 封装底部导航栏
"""
from common.base_page import BasePage


class MainPage(BasePage):
    """
    nav_main: 底部导航栏-首页
    nav_category: 底部导航栏-分类
    nav_find: 底部导航栏-发现
    nav_cart: 底部导航栏-购物车
    nav_my: 底部导航栏-我的
    """
    nav_main = ('id', 'com.mimu.mshop:id/homeFragment')
    nav_category = ('id', 'com.mimu.mshop:id/sortFragment')
    nav_find = ('id', 'com.mimu.mshop:id/findFragment')
    nav_cart = ('id', 'com.mimu.mshop:id/shopFragment')
    nav_my = ('id', 'com.mimu.mshop:id/mineFragment')
    # 首页金刚区-超市按钮
    vajra_market_icon = ("id", "com.mimu.mshop:id/tv_name", 0)
    # 首页金刚区-餐厅按钮
    vajra_restaurant_icon = ("id", "com.mimu.mshop:id/tv_name", 1)
    # 首页金刚区-门店按钮
    vajra_offline_icon = ("id", "com.mimu.mshop:id/tv_name", 2)
    # 首页金刚区-优惠券按钮
    vajra_coupon_icon = ("id", "com.mimu.mshop:id/tv_name", 3)
    # 首页金刚区-会员按钮
    vajra_vip_icon = ("id", "com.mimu.mshop:id/tv_name", 4)
    # 返回按钮
    back_button = ('id', 'com.mimu.mshop:id/back')
    # 顶部扫一扫按钮
    header_scan = ('id', 'com.mimu.mshop:id/img_scan')
    # 顶部二维码按钮
    header_qrcode = ('id', 'com.mimu.mshop:id/img_qCode')
    # 顶部消息按钮
    header_message = ('id', 'com.mimu.mshop:id/img_msg')

    # 定义底部导航栏方法
    def main_nav(self):
        """
        点击底部导航栏首页
        """
        self.click(self.nav_main, '底部导航栏-首页')

    def category_nav(self):
        """
        点击底部导航栏分类
        """
        self.click(self.nav_category, '底部导航栏-分类')

    def find_nav(self):
        """
        点击底部导航栏发现
        """
        self.click(self.nav_find, '底部导航栏-发现')

    def cart_nav(self):
        """
        点击底部导航栏购物车
        """
        self.click(self.nav_cart, '底部导航栏-购物车')

    def my_nav(self):
        """
        点击底部导航栏我的
        """
        self.click(self.nav_my, '底部导航栏-我的')

    # 定义金刚区方法
    def enter_market_page(self):
        """
        点击首页超市按钮
        """
        self.click(self.vajra_market_icon, '点击首页超市按钮')

    def enter_restaurant_page(self):
        """
        点击首页餐厅按钮
        """
        self.click(self.vajra_restaurant_icon, '点击首页餐厅按钮')

    def enter_offline_page(self):
        """
        点击首页门店按钮
        """
        self.click(self.vajra_offline_icon, '点击首页门店按钮')

    def enter_coupon_page(self):
        """
        点击首页优惠券按钮
        """
        self.click(self.vajra_coupon_icon, '点击首页优惠券按钮')

    def enter_vip_page(self):
        """
        点击首页会员按钮
        """
        self.click(self.vajra_vip_icon, '点击首页会员按钮')

    # 定义header区域方法
    def scan(self):
        """
        点击扫一扫按钮
        """
        self.click(self.header_scan, '点击扫一扫按钮')

    def qrcode(self):
        """
        点击二维码按钮
        """
        self.click(self.header_qrcode, '点击二维码按钮')

    def message(self):
        """
        点击消息按钮
        """
        self.click(self.header_message, '点击消息按钮')
