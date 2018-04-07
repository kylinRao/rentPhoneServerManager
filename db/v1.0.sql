DROP TABLE IF EXISTS rentLog;
CREATE TABLE rentLog(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,-- 使用者姓名
phone TEXT,--   使用者的电话号码，方便管理者联系到使用者
rentPhoneType TEXT,----当前手机的型号，如荣耀V8等
deviceId TEXT,----当前手机的imei号
status int,--当前手机状态，0表示已结束流程，1表示借出状态
returnName TEXT,-- 使用者姓名
returnPhone TEXT,--   使用者的电话号码，方便管理者联系到使用者
rentTime DATA DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')),
returnTime DATA DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')),
battaryLevel int,---当前手机的电量信息
gameboxVersion TEXT, ---当前手机的游戏中心版本号信息
hiappVersion  TEXT, --当前手机应用市场的版本号信息
hmsVersion   TEXT  ---当前手机华为移动服务的版本号信息
);
DROP TRIGGER IF EXISTS deleteSomeThing;

CREATE TRIGGER deleteSomeThing
         AFTER INSERT
            ON rentLog
      FOR EACH ROW
          WHEN (
                   SELECT count(1)
                     FROM rentlog
               )
> 20000
BEGIN
    DELETE FROM rentlog
          WHERE date(rentTime) < date('now', '-60 day');
END;




DROP TABLE IF EXISTS devices;
CREATE TABLE devices(
rentPhoneType TEXT,----当前手机的型号，如荣耀V8等
deviceName TEXT,-----设备的中文名字
deviceId TEXT PRIMARY KEY ,----设备标识
renterName TEXT,-- 使用者姓名
status boolean ,--当前手机状态，0表示已结束流程，1表示借出状态
isRoot boolean,------当前手机是否root了
gameboxVersion TEXT, ---当前手机的游戏中心版本号信息
hiappVersion  TEXT, --当前手机应用市场的版本号信息
hmsVersion   TEXT,  ---当前手机华为移动服务的版本号信息
owner TEXT ---设备所有者
-- foreign key(owner) references users(name)

);

DROP TABLE IF EXISTS roles_users;
DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS users;
