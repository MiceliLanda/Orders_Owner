
from fastapi import APIRouter
from config.db import conn,session
from models.order import tableOrder, tableOrderDetails, tableMenu, tableSaucer, tableShop, tableOwner,tableUser
from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy import select
from config.db import conn

orderRoute = APIRouter()

@orderRoute.get("/owner/order/pending/{shop_id}")
async def rechargeCredits(shops_id: int):
    try:
        query = select([tableOrder.c.id, tableOrder.c.status, tableOrder.c.user_id, tableShop.c.name, tableUser.c.name, tableSaucer.c.name]).select_from(tableOrder).join(tableOrderDetails,tableOrder.c.id == tableOrderDetails.c.order_id).join(tableSaucer,tableSaucer.c.id==tableOrderDetails.c.saucer_id).join(tableMenu,tableSaucer.c.menu_id == tableMenu.c.id).join(tableShop,tableMenu.c.shop_id == tableShop.c.id).join(tableUser,tableOrder.c.user_id == tableUser.c.id).where(tableOrder.c.status == 0).where(tableShop.c.id == shops_id)
        result = session.execute(query).fetchall()
        data = []
        for row in result:
            data.append({"id_orden":row[0],"status":row[1],"user_id":row[2],"shop_name":row[3],"user_name":row[4],"saucer_name":row[5]})
        return JSONResponse(status_code=status.HTTP_200_OK, content=data)
    except Exception as e:
        return {"Error":str(e)}

@orderRoute.put("/owner/order/inprogres/{orden_id}")
async def preparingOrder(orden_id: int):
    try:
        query = tableOrder.update().where(tableOrder.c.id == orden_id).values(status=1)
        session.execute(query)
        return {"status":"Orden en proceso"}
    except Exception as e:
        return {"Error":str(e)}      

@orderRoute.put("/owner/order/completed/{orden_id}")
async def orderCompleted(orden_id: int):
    try:
        query = tableOrder.update().where(tableOrder.c.id == orden_id).values(status=2)
        session.execute(query)
        return {"status":"Puedes pasar a recoger la orden"}
    except Exception as e:
        return {"Error":str(e)}

@orderRoute.get("/owner/orders/{shop_id}")
async def getOrdersPushNotifications(shop_id: int):
    try:
        query = select([tableOrder.c.id, tableOrder.c.status, tableOrder.c.user_id, tableShop.c.name, tableUser.c.name, tableSaucer.c.name]).select_from(tableOrder).join(tableOrderDetails,tableOrder.c.id == tableOrderDetails.c.order_id).join(tableSaucer,tableSaucer.c.id==tableOrderDetails.c.saucer_id).join(tableMenu,tableSaucer.c.menu_id == tableMenu.c.id).join(tableShop,tableMenu.c.shop_id == tableShop.c.id).join(tableUser,tableOrder.c.user_id == tableUser.c.id).where(tableOrder.c.status == 2).where(tableShop.c.id == shop_id)
        result = session.execute(query).fetchall()
        data = []
        for row in result:
            data.append({"id_orden":row[0],"status":row[1],"user_id":row[2],"shop_name":row[3],"user_name":row[4],"saucer_name":row[5]})
        return JSONResponse(status_code=status.HTTP_200_OK, content=data)
    except Exception as e:
        return {"Error":str(e)}