import os


class Config:
	SECRET_KEY = '74cfe9519ac69de16029f20e2786f1e5'
	# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:ehr2password@aahn9mlfrrvcm5.cacrvcq7qcsm.us-east-2.rds.amazonaws.com:3306/ebdb' 
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	SQLALCHEMY_DATABASE_URI = 'postgres://ixrnfgkwonyroj:6c3743e4ae27871ed778b70e5524bb16f6378937e667957f32dd599b25fde0ed@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d518tfe57nmff3'

