# EnumAggregatorTheadPool
```
 package com.aihuishou.service.tic.enumerate;

import com.aihuishou.common.pattern.aggregator.poll.EnumTheadPoolKey;
import com.aihuishou.common.pattern.aggregator.poll.ThreadPoolExecutorProperty;

public enum EnumAggregatorTheadPool implements EnumTheadPoolKey {
    ORDER("orderPoll") {
        @Override
        public ThreadPoolExecutorProperty getProperty() {
            return ThreadPoolExecutorProperty.builder()
                .corePoolSize(20)
                .maxPollSize(50)
                .queueCapacity(1000)
                .build();
        }
    },
    TMP("tmpPoll") {
        @Override
        public ThreadPoolExecutorProperty getProperty() {
            return ThreadPoolExecutorProperty.builder()
                .corePoolSize(20)
                .maxPollSize(30)
                .queueCapacity(1000)
                .build();
        }
    },
    ;

    private final String prefixName;

    EnumAggregatorTheadPool(String prefixName) {
        this.prefixName = prefixName;
    }


    @Override
    public String getKey() {
        return this.name();
    }

    @Override
    public String getThreadNamePrefix() {
        return this.prefixName;
    }
}
 ```
# EnumPickupTypeMapping
```
 package com.aihuishou.service.tic.enumerate;

import com.aihuishou.core.service.order.own.model.constant.EnumPickUpType;
import com.aihuishou.service.tic.model.enumerate.EnumGenericPickupType;

import java.util.Objects;

public enum EnumPickupTypeMapping {
    ON_DOOR(EnumGenericPickupType.ONDOOR, EnumPickUpType.ONDOOR),
    SHOP(EnumGenericPickupType.SHOP, EnumPickUpType.SHOP),
    O2O_SHOP(EnumGenericPickupType.O2O_SHOP, EnumPickUpType.SHOP),
    ;

    private EnumGenericPickupType tradeInOrderPickupType;
    private EnumPickUpType pickUpType;

    public EnumGenericPickupType getTradeInOrderPickupType() {
        return tradeInOrderPickupType;
    }

    public EnumPickUpType getPickUpType() {
        return pickUpType;
    }

    EnumPickupTypeMapping(EnumGenericPickupType tradeInOrderPickupType, EnumPickUpType pickUpType) {
        this.tradeInOrderPickupType = tradeInOrderPickupType;
        this.pickUpType = pickUpType;
    }

    public static EnumPickupTypeMapping getByPickupType(Integer pickupType) {
        for (EnumPickupTypeMapping mapping : values()) {
            if (Objects.equals(mapping.getPickUpType().getValue(), pickupType)) {
                return mapping;
            }
        }
        return null;
    }
}
 ```
# EnumTradeInOrderConfirmation
```
 package com.aihuishou.service.tic.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

/**
 * 标记预约类型
 */
public enum EnumTradeInOrderConfirmation implements DocumentedEnum<Integer> {
    CONFIRMATION_NOT_NEEDED(1, "普通单"),
    CONFIRMATION_NEEDED(2, "预约单");

    private Integer document;
    private String desc;

    EnumTradeInOrderConfirmation(Integer document, String desc) {
        this.document = document;
        this.desc = desc;
    }

    @Override
    public Integer getDocument() {
        return document;
    }

    public String getDesc() {
        return desc;
    }
} ```
# EnumWorkerType
```
 package com.aihuishou.service.tic.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;
import com.aihuishou.common.worker.model.IWorkerType;

public enum EnumWorkerType implements DocumentedEnum<Integer>, IWorkerType {
    APPOINTMENT_DISPATCH_BILL(1, "", "更新上门服务单预约时间"),
    COOP_PACKAGE_CHANGE_EXPRESS_NO(2, "", "京东重复发货且物流单号变更"),
    DING_MESSAGE(3, "", "钉钉消息"),
    CLOSE_EXTERNAL_STOCK_TRANSFER_BILL_WORKER(4, "", "取消出库单"),
    SUPPLIER_DISPATCH_ORDER_CREATE(5, "", "创建供应商发货单"),
    SUPPLIER_DISPATCH_ORDER_NOTIFY_TIC(6, "", "发货单动作通知TIC-Order"),
    SUPPLIER_PACKAGE_RECEIVED(7, "", "创建供应商物流包裹"),
    ORL_ORDER_VALIDATED(8, "", "旧机验货"),
    ORDER_REFUND_WALLET_CHARGE(100, "", "订单退款钱包打款给用户"),
    ;

    private final Integer document;
    private final String tag;
    private final String desc;

    EnumWorkerType(Integer document, String tag, String desc) {
        this.document = document;
        this.tag = tag;
        this.desc = desc;
    }

    @Override
    public Integer getDocument() {
        return document;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    @Override
    public Integer getType() {
        return document;
    }

    @Override
    public String getTag() {
        return tag;
    }
}
 ```
# EnumTradeInOrderProcess
```
 package com.aihuishou.service.tic.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

/**
 * 订单流程枚举
 */
public enum EnumTradeInOrderProcess implements DocumentedEnum<Integer> {
    AHS_OFFICIAL_O2O(1, "爱回收官网O2O换新订单流程"),
    AHS_OFFICIAL_ON_DOOR(2, "爱回收官网上门换新订单流程"),
    AHS_VIRTUAL(3, "爱回收虚拟订单流程"),

    AHS_OFFICIAL_O2O_MAY_RECYCLE(4, "爱回收官网O2O可能包含旧机换新订单流程"),
    AHS_OFFICIAL_O2O_NOT_RECYCLE(5, "爱回收官网O2O无旧机换新订单流程"),
    AHS_SUPPLIER_O2O_MAY_RECYCLE(6, "爱回收供应商O2O可能包含旧机换新订单流程"),
    AHS_SUPPLIER_O2O_NOT_RECYCLE(7, "爱回收供应商O2O无旧机换新订单流程"),
    AHS_SUPPLIER_DELIVER(8, "爱回收供应商快递销售订单流程"),

    AHS_SHOP_WITH_STOCK(101, "爱回收门店有库存销售订单流程"),
    AHS_SHOP_WITHOUT_STOCK(102, "爱回收门店无库存销售订单流程"),
    AHS_TYING_ON_DOOR(103, "爱回收搭售上门销售订单流程"),

    AHS_SHOP_TRADE_IN(104, "爱回收门店换新订单流程"),

    SHARE_FQL_O2O(201, "官网共享式分期乐O2O换新订单流程"),
    SHARE_FQL_ON_DOOR(202, "官网共享式分期乐上门换新订单流程"),

    ONE_STOP_O2O(501, "一站换新O2O订单流程"),
    ONE_STOP_ON_DOOR(502, "一站换新上门订单流程"),
    ;


    private final Integer document;
    private final String desc;

    EnumTradeInOrderProcess(Integer document, String desc) {
        this.document = document;
        this.desc = desc;
    }

    @Override
    public Integer getDocument() {
        return document;
    }

    @Override
    public String getDesc() {
        return desc;
    }
}
 ```
