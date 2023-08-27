class Settings:
    """存储所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕
        self.screen_width = 1200
        self.screen_height = 780
        self.bg_color = (230, 230, 230)  # 书例程颜色

        # self.bg_color = (135, 206, 250)# 练习12-1：蓝色天空背景
        # self.bg_color = (254, 192, 236)  # 练习12-2：角色背景

        self.win_caption = "外星人入侵"
        self.ship_speed = 1.5  # 飞船移动速度设置

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
