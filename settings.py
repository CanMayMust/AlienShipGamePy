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
        self.ship_speed = 1.0  # 飞船移动速度设置

        # 子弹设置
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1为向右，-1为向左（人面对屏幕为基准）
        self.fleet_direction = 1
