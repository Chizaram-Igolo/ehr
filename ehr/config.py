import os


class Config:
	SECRET_KEY = '74cfe9519ac69de16029f20e2786f1e5'
	# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:ehr2password@aahn9mlfrrvcm5.cacrvcq7qcsm.us-east-2.rds.amazonaws.com:3306/ebdb' 
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	SQLALCHEMY_DATABASE_URI = 'postgres://pvrsmkusylwhgk:bbd8018d93372752c8eb5397352e6b5997cf89f4fdcf876907df313b4bbfcb44@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d7tb0tb2cjde8h'

