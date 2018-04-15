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


-- ########################南京房价数据表定义##############################

-- DROP TABLE IF EXISTS houseBaseInfo;
-- CREATE TABLE houseBaseInfo(
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- houseId INT UNIQUE ,
-- houseInfo TEXT,-- 房屋的基本信息
-- publishday INT DEFAULT 0,----一共发布了多少天
-- url TEXT,----详情连接地址
-- visited int,--当前共计多少访问量
-- region TEXT,-- 地区分布
-- area TEXT,---分区，如鼓楼，等
-- attention INT ,--   关注度
-- sourceId int---数据来自于哪个房产交易所
-- );
-- DROP TABLE IF EXISTS houseSource;
-- CREATE TABLE houseSource(
-- sourceId INTEGER PRIMARY KEY AUTOINCREMENT,
-- sourceDes TEXT-------鼓楼 建邺 秦淮 玄武 雨花台 栖霞 江宁 浦口 六合 溧水 高淳
-- );
--
--
-- DROP TABLE IF EXISTS houseEveryDayPrice;
-- CREATE TABLE houseEveryDayPrice(
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- houseCode INT ,
-- date date,-- 房屋价格记录的当天
-- totalPrice FLOAT ,--   整套房子的总价个
-- unitPrice FLOAT,---每平方米单价/
-- updateTime datetime
-- );
-- create unique index houseId_date on houseEveryDayPrice(houseCode,date);
-- -- 统计报表
-- DROP TABLE IF EXISTS houseReduceDay;
-- CREATE TABLE houseReduceDay(
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- houseId INT ,
-- date date,-- 房屋价格记录的当天
-- reducePercent FLOAT -- 降价百分比
-- );
-- DROP TABLE IF EXISTS houseReduceWeek;
-- CREATE TABLE houseReduceWeek(
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- houseId INT ,
-- date date,-- 房屋价格记录的当天
-- reducePercent FLOAT -- 降价百分比
-- );
-- DROP TABLE IF EXISTS houseReduceMonth;
-- CREATE TABLE houseReduceMonth(
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- houseId INT ,
-- date date,-- 房屋价格记录的当天
-- reducePercent FLOAT -- 降价百分比
-- );
-- DROP TABLE IF EXISTS HouseReduceUntilNow;
-- CREATE TABLE HouseReduceUntilNow(
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- houseId INT ,
-- date date,-- 房屋价格记录的当天
-- reducePercent FLOAT -- 降价百分比
-- );
-- 房屋详细信息表
-- DROP TABLE IF EXISTS houseDetailInfo;
-- CREATE TABLE houseDetailInfo(
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- houseId INT UNIQUE ,
-- date date,-- 房屋价格记录的当天
-- houseNumType TEXT,---房子几室几厅
-- houseHeight  TEXT,-----房子楼层情况
-- houseBigSquare TEXT,---房子总面积
-- houseInnerSquare  TEXT,---房子套内面积
-- houseStuctType  TEXT,---房子是板楼还是调高什么的
-- houseDirctionType  TEXT,---房子的朝向
-- houseStuctMaterialType  TEXT,---房子是钢筋水泥的还是什么的
-- houseDecrateType  TEXT,---房子装修情况
-- houseIsWithLift  TEXT,---房子是否有电梯
-- houseRightYear  TEXT,---房子的产权一共是多少年
--
--
-- tradeOnlineTime  DATE ,---房子发布交易的时间
-- tradeRightType  TEXT,---房子的交易类型是商品房还是什么房子
-- tradeLastTime  DATE,---房子上次交易时间
-- tradeUseType  TEXT,---房子用途，一般是普通住宅
-- tradeLostTime  TEXT,---房子的年限是满两年还是满五年
-- tradeHouseRightOwnType  TEXT,---是共有产品还是什么产权房子
-- tradeGurantyMsg  TEXT,---房子抵押信息
-- tradeHouseBookMsg  TEXT---房本信息
-- );


































