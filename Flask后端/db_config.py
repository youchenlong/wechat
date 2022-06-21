from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# flask应用实例
app = Flask(__name__)

# 数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/wechat"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db_init = SQLAlchemy(app)