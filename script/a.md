# EnumCoopOrderType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumCoopOrderType implements DocumentedEnum<Integer> {
    SAMSUNG(1, "三星"),
    FEN_QI_LE(2, "分期乐"),
    JD_ONE_STOP(3, "京东一站式"),
    SHARE_FEN_QI_LE(4, "共享式分期乐"),
    HUA_SHENG(5, "联通华盛"),
    HUA_WEI(6, "华为"),
    ;

    private final Integer document;
    private final String desc;

    EnumCoopOrderType(Integer document, String desc) {
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
# EnumVendorType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumVendorType implements DocumentedEnum<Integer> {
    AHS(1, "爱回收商户"),
    FRANCHISEE(2, "加盟商户"),
    ;

    private final Integer document;
    private final String desc;

    EnumVendorType(Integer document, String desc) {
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
# EnumSubsidyStatus
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumSubsidyStatus implements DocumentedEnum<Integer> {
    ENABLED(1, "启用"),
    DISABLED(2, "关闭");

    private int value;
    private String desc;

    public int getValue() {
        return value;
    }

    @Override
    public Integer getDocument() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    EnumSubsidyStatus(int value, String desc) {
        this.value = value;
        this.desc = desc;
    }
}
 ```
# EnumTradeInOrderCancelReason
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public enum EnumTradeInOrderCancelReason implements DocumentedEnum<Integer> {
    SYSTEM_1(1, 3, "系统原因", 13, "其他原因"),
    SYSTEM_2(2, 3, "合作方取消", 13, "其他原因"),
    CUSTOMER_3(3, 1, "交易时间/地点不方便", 4, "交易时间不方便"),
    CUSTOMER_4(4, 1, "已在其它地方购买新机", 25, "卖给其他回收商"),
    CUSTOMER_5(5, 1, "旧机价格过低", 32, "价格不符合预期"),
    CUSTOMER_6(6, 1, "服务不满意", 33, "工作人员服务态度差"),
    CUSTOMER_7(7, 1, "其它原因", 13, "其它原因"),
    ERP_8(8, 2, "测试/重复/错误订单", 51, "测试订单"),
    ERP_9(9, 2, "交易时间/地点不方便", 4, "交易时间不方便"),
    ERP_10(10, 2, "不想换了", 26, "自己留用"),
    ERP_11(11, 2, "旧机回收价格不满意", 32, "价格不符合预期"),
    ERP_12(12, 2, "修改支付方式/SKU/订单类型", 40, "机器描述有误"),
    ERP_13(13, 2, "已在其它地方换新", 25, "卖给其他回收商"),
    ERP_14(14, 2, "其它原因", 13, "其它原因"),
    SYSTEM_15(15, 3, "超时", 7, "逾期自动取消"),
    CUSTOMER_16(16, 1, "不小心提交", 52, "下单错误"),
    CUSTOMER_17(17, 1, "订单信息填写错误", 52, "下单错误"),
    ;

    private Integer value;
    private Integer type;
    private String desc;
    private Integer oldProductValue;
    private String oldProductDesc;

    @Override
    public Integer getDocument() {
        return value;
    }

    public Integer getValue() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    public Integer getType() {
        return type;
    }

    public Integer getOldProductValue() {
        return oldProductValue;
    }

    public String getOldProductDesc() {
        return oldProductDesc;
    }

    EnumTradeInOrderCancelReason(Integer value, Integer type, String desc, Integer oldProductValue, String oldProductDesc) {
        this.value = value;
        this.type = type;
        this.desc = desc;
        this.oldProductValue = oldProductValue;
        this.oldProductDesc = oldProductDesc;
    }

    public static List<EnumTradeInOrderCancelReason> erpReasons() {
        return Stream.of(values()).filter(reason -> reason.getType() == 2).collect(Collectors.toList());
    }

    public static List<EnumTradeInOrderCancelReason> userReasons() {
        return Stream.of(values()).filter(reason -> reason.getType() == 1).collect(Collectors.toList());
    }

    public static List<EnumTradeInOrderCancelReason> systemReasons() {
        return Stream.of(values()).filter(reason -> reason.getType() == 3).collect(Collectors.toList());
    }

    public static EnumTradeInOrderCancelReason getByValue(Integer value) {
        if (null == value) {
            return null;
        }
        for (EnumTradeInOrderCancelReason reason : values()) {
            if (Objects.equals(reason.getValue(), value)) {
                return reason;
            }
        }
        return null;
    }
}
 ```
# EnumBaseTradeInOrderType
```
 package com.aihuishou.service.tic.model.enumerate;


import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumBaseTradeInOrderType implements DocumentedEnum<String> {
    ONE_STOP_TRADE_IN_ORDER("OneStopTradeInOrder", "一站式以旧换新", 1),
    AHS_TRADE_IN_ORDER("AhsTradeInOrder", "官网以旧换新", 2),
    FQL_SHARE_TRADE_IN_ORDER("FqlShareTradeInOrder", "共享式以旧换新", 3),
    ;

    private final String document;
    private final String desc;
    private final Integer value;

    EnumBaseTradeInOrderType(final String document, final String desc, final Integer value) {
        this.document = document;
        this.desc = desc;
        this.value = value;
    }

    @Override
    public String getDocument() {
        return document;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    public Integer getValue() {
        return value;
    }
}
 ```
# EnumPackageDeliverType
```
 package com.aihuishou.service.tic.model.enumerate;


import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumPackageDeliverType implements DocumentedEnum<Integer> {
    AHS(1, "AHS配送"),
    PARTNER(2, "厂商配送"),
    NONE(3, "无需配送"),
    ;
    private final Integer value;
    private final String desc;

    public Integer getValue() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    EnumPackageDeliverType(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }

    @Override
    public Integer getDocument() {
        return this.value;
    }
}
 ```
# EnumTradeInOrderTransactionCloseStatus
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumTradeInOrderTransactionCloseStatus implements DocumentedEnum<Integer> {
    NO_CLOSE(0, "未关闭"),
    CLOSE(1, "关闭"),
    ;

    private final Integer document;
    private final String desc;

    EnumTradeInOrderTransactionCloseStatus(Integer document, String desc) {
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
# EnumShopV2Type
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

import java.util.Objects;

/**
 * 为了解决sonar的问题而专门设置的V2版本，TODO:cj 后续再用回EnumShopType名称
 *
 * @author chujun
 */

public enum EnumShopV2Type implements DocumentedEnum<Integer> {
    ONLINE_SHOP(1, "线上门店"),
    OFFLINE(2, "线下门店"),
    COOP_MARKET(3, "CoopMarket"),
    XIAO_MI_SHOP(4, "小米门店"),
    JD_SHOP(5, "京东门店"),
    OFFLINE_LEAGUE_SHOP(6, "线下加盟店"),
    ;
    private Integer value;
    private String desc;

    public Integer getValue() {
        return value;
    }

    @Override
    public Integer getDocument() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    EnumShopV2Type(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }

    public static EnumShopV2Type getByValue(Integer value) {
        if (null == value) {
            return null;
        }
        for (EnumShopV2Type status : values()) {
            if (Objects.equals(status.getValue(), value)) {
                return status;
            }
        }
        return null;
    }
}
 ```
# EnumTradeInOrderRefundReason
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

import java.util.Objects;

public enum EnumTradeInOrderRefundReason implements DocumentedEnum<Integer> {
    REFUND_TYPE_NO_REASON(1, "不想买了", 10),
    REFUND_TYPE_WRONG_PRODUCT(2, "手机机型选错", 12),
    REFUND_TYPE_RETURN_FOOD(4, "退货退款", 14),
    REFUND_TYPE_OTHER(3, "其他", 14),
    ;

    private Integer value;
    private String desc;
    private Integer cancelReasonValue;

    public Integer getValue() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    public Integer getCancelReasonValue() {
        return cancelReasonValue;
    }

    @Override
    public Integer getDocument() {
        return value;
    }

    EnumTradeInOrderRefundReason(Integer value, String desc, Integer cancelReasonValue) {
        this.value = value;
        this.desc = desc;
        this.cancelReasonValue = cancelReasonValue;
    }

    public static EnumTradeInOrderRefundReason getByValue(Integer value) {
        if (null == value) {
            return null;
        }
        for (EnumTradeInOrderRefundReason status : values()) {
            if (Objects.equals(status.getValue(), value)) {
                return status;
            }
        }
        return null;
    }


}
 ```
# EnumTradeInOrderAction
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumTradeInOrderAction implements DocumentedEnum<Integer> {
    //TODO:cj to be confirmed 判断 流程流向动作使用情况
    //used
    COOP_DELIVER(1, "合作方发货"),
    //used
    PAY(2, "支付"),
    //used
    CANCEL(3, "取消"),
    //used
    RECEIVE(4, "收货"),
    CONFIRM_ONDOOR(5, "确认上门信息"),
    //used
    DISPATCH(6, "派单"),
    //used
    STOCK_OUT(7, "出库"),
    //TODO:cj to be done 官网订单使用旧机完结替换，BD订单还是这个消息
    //used
    OLD_ORDER_VALIDATE(8, "验货"),
    OLD_ORDER_SETTLE(9, "旧机结算"),
    SETTLE_START(10, "结算开始"),
    //used //TODO:cj 还是先按照结算完成动作处理吧,保持兼容性
    SETTLE_FINISH(11, "结算完成"),
    //used
    VERIFICATE(12, "核销"),
    APPLY_RETURN(13, "申请退货"),
    APPEND_APPLY_RETURN(14, "附加退货信息"),
    //used
    REFUND(15, "退款成功"),
    CREATE_ORDER(16, "创建订单"),
    MANUAL_ASSOCIATE_PACKAGE_EXPRESS(17, "关联包裹物流单号"),
    //used
    RETURN(18, "退货完成"),
    COOP_PAY(19, "合作方支付"),
    PRE_PAY(20, "预支付"),


    //TODO:cj used added
    OLD_ORDER_FINAL(21, "旧机完结"),
    ;

    private final Integer document;
    private final String desc;

    EnumTradeInOrderAction(Integer document, String desc) {
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
# InvoiceRequestNotApplicableReason
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum InvoiceRequestNotApplicableReason implements DocumentedEnum<Integer> {
    NOT_APPLICABLE_CODE_DUPLICATED_REQUEST(1, "已开票"),
    NOT_APPLICABLE_CODE_ORDER_STATUS(2, "订单状态异常"),
    NOT_APPLICABLE_CODE_ORDER_AMOUNT(3, "开票金额异常"),
    NOT_APPLICABLE_CODE_AMOUNT_LIMIT(4, "开票金额过大"),
    NOT_APPLICABLE_CODE_EXIST_AFTER_SALE_ORDER(5, "存在售后单"),
    NOT_APPLICABLE_CODE_NOT_SUPPORT_FRANCHISEE_VENDOR(6, "加盟商订单不支持开票"),
    NOT_APPLICABLE_CODE_ORDER_TIME_OUTDATED(101, "2018-11-15 12:00:00 前订单不可开具发票"),
    NOT_APPLICABLE_CODE_PAID_DATE_EXPIRED(102, "180 天前付款订单不可开票"),

    ;

    private final Integer document;
    private final String desc;

    InvoiceRequestNotApplicableReason(Integer document, String desc) {
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
# EnumBDTradeInOrderSettleType
```
 package com.aihuishou.service.tic.model.enumerate;


import com.aihuishou.common.model.constant.DocumentedEnum;

/**
 * 站在爱回收角度出发
 */
public enum EnumBDTradeInOrderSettleType implements DocumentedEnum<Integer> {
    PAY(1, "付款", "用户"),
    RECEIPT(2, "收款", "爱回收"),
    BALANCE(3, "收支平衡", null),
    ;

    private final Integer document;
    private final String desc;
    // 收款人
    private final String payee;

    @Override
    public Integer getDocument() {
        return document;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    public String getPayee() {
        return payee;
    }

    EnumBDTradeInOrderSettleType(Integer document, String desc, String payee) {
        this.document = document;
        this.desc = desc;
        this.payee = payee;
    }

    public static EnumBDTradeInOrderSettleType getByUserPayAmount(Integer actualUserPayAmount) {
        if (actualUserPayAmount > 0) {
            return EnumBDTradeInOrderSettleType.RECEIPT;
        } else if (actualUserPayAmount < 0) {
            return EnumBDTradeInOrderSettleType.PAY;
        } else {
            return EnumBDTradeInOrderSettleType.BALANCE;
        }
    }
}
 ```
# EnumTradeInOrderGiftStatus
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumTradeInOrderGiftStatus implements DocumentedEnum<Integer> {
    PENDING(1, "等待发放"),
    DELIVERING(2, "发放中"),
    DELIVERED(3, "已发放"),
    FAILED(4, "发放失败");

    private final Integer document;
    private final String desc;

    EnumTradeInOrderGiftStatus(Integer document, String desc) {
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
# EnumGenericPickupType
```
 package com.aihuishou.service.tic.model.enumerate;


import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumGenericPickupType implements DocumentedEnum<Integer> {
    NO_NEED_PICKUP(0, "无需取货", null),
    ONDOOR(1, "上门", 1),
    METRO(2, "地铁", 2),
    DELIVER(4, "快递", 4),
    SHOP(5, "门店", 5),
    MTA(6, "MTA", 6),
    O2O_SHOP(7, "O2O门店", 5),
    ;

    private final Integer document;
    private final String desc;
    private final Integer recycleOrderPickupType;

    EnumGenericPickupType(Integer document, String desc, Integer recycleOrderPickupType) {
        this.document = document;
        this.desc = desc;
        this.recycleOrderPickupType = recycleOrderPickupType;
    }

    @Override
    public Integer getDocument() {
        return document;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    public Integer getRecycleOrderPickupType() {
        return recycleOrderPickupType;
    }
}
 ```
# EnumBaseTradeInOrderStatus
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.exception.ServiceException;
import com.aihuishou.common.model.constant.DocumentedEnum;
import com.google.common.collect.Sets;

import java.util.Date;
import java.util.Objects;
import java.util.Set;

public enum EnumBaseTradeInOrderStatus implements DocumentedEnum<Integer> {
    TO_BE_PAID(0, "待付款"),
    TO_BE_DELIVER(1, "待发货"),
    TO_BE_RECEIVE(10, "待门店收货"),
    TO_BE_DISPATCH(20, "待派单"),
    TO_BE_ON_DOOR(30, "待上门"),
    TO_BE_INSPECT(40, "待核验"),
    TO_BE_SETTLE(50, "待结算"),
    TO_BE_HAND_OVER(60, "待客人收货"),
    //不再使用了
    TO_BE_CONFIRMED(70, "待确认"),
    SUCCESS(100, "交易完成"),
    CANCELLED(120, "已取消"),
    //售后退货交易关闭
    RETURNED(200, "已退货"),
    ;

    private final Integer document;
    private final String desc;

    EnumBaseTradeInOrderStatus(Integer document, String desc) {
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

    public static Set<EnumBaseTradeInOrderStatus> getFinalStatus() {
        return Sets.newHashSet(EnumBaseTradeInOrderStatus.CANCELLED, EnumBaseTradeInOrderStatus.SUCCESS);
    }

    /**
     * TODO:cj 后续删除
     * 供上游使用
     */
    public static Integer convertToCoralOrderStatus(Integer pickupType, Integer baseTradeInOrderStatus, Date refundedDt) {
        //经过和小华确认，目前前端只用到老状态的31(待核验状态)和3(已完成)，策略其他只都返回原值，这两个状态转化尽量保证正确
        if (null == baseTradeInOrderStatus) {
            throw ServiceException.ofMessage("无法转化订单状态,baseTradeInOrderStatus="
                + baseTradeInOrderStatus + ",pickupType=" + pickupType + ",refundedDt=" + refundedDt);
        }
        if (Objects.equals(EnumBaseTradeInOrderStatus.TO_BE_INSPECT.getDocument(), baseTradeInOrderStatus)) {
            return EnumTradeInOrderStatus.RECYCLE_INSPECT_PENDING.getValue();
        } else if (Objects.equals(EnumBaseTradeInOrderStatus.SUCCESS.getDocument(), baseTradeInOrderStatus)) {
            return EnumTradeInOrderStatus.COMPLETED.getValue();
        } else if (Objects.equals(EnumBaseTradeInOrderStatus.TO_BE_DISPATCH.getDocument(), baseTradeInOrderStatus)
            || Objects.equals(EnumBaseTradeInOrderStatus.TO_BE_ON_DOOR.getDocument(), baseTradeInOrderStatus)) {
            //官网订单
            if (Objects.equals(EnumGenericPickupType.ONDOOR.getDocument(), pickupType)) {
                return EnumTradeInOrderStatus.RECYCLE_INSPECT_PENDING.getValue();
            }
        }
        //默认则返回原始的订单状态
        return baseTradeInOrderStatus;
    }
}
 ```
# EnumTradeInOrderTransactionGatewayType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;
import io.swagger.annotations.ApiModel;

/**
 * @author chujun
 */

@ApiModel(description = "新机支付流水类型")
public enum EnumTradeInOrderTransactionGatewayType implements DocumentedEnum<Integer> {
    ALIPAY(1, "支付宝", "1001", "1011"),
    WECHAT(2, "微信", "1002", "1004"),
    ACCOUNT(3, "爱回收钱包", null, null),
    FQL_CREDIT(4, "分期乐信用额度", null, null),
    CASH(5, "现金", null, null),
    ;

    private Integer document;
    private String desc;
    private String receiptGateway;
    private String payGateway;

    EnumTradeInOrderTransactionGatewayType(Integer document, String desc, String receiptGateway, String payGateway) {
        this.document = document;
        this.desc = desc;
        this.receiptGateway = receiptGateway;
        this.payGateway = payGateway;
    }

    @Override
    public Integer getDocument() {
        return document;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    public String getPayGateway() {
        return payGateway;
    }

    public String getReceiptGateway() {
        return receiptGateway;
    }
}
 ```
# EnumBaseTradeInOrderStockType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

/**
 * 库存类型,和sale-order EnumSaleOrderDetailStockType 保持一致
 */
public enum EnumBaseTradeInOrderStockType implements DocumentedEnum<Integer> {
    /**
     * 不校验库存
     */
    UNCHECKED_STOCK(1, "不校验库存"),
    /**
     * 爱回收库存
     */
    AHS_STOCK(2, "爱回收库存"),
    /**
     * 合作方库存
     */
    PARTNER_STOCK(3, "合作方库存"),
    ;

    private final Integer document;
    private final String desc;

    EnumBaseTradeInOrderStockType(Integer document, String desc) {
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
# EnumOverlayType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

import java.util.Objects;

/**
 * @author chujun
 */

public enum EnumOverlayType implements DocumentedEnum<Integer> {
    SQUARE(1, "方形"),
    CIRCULAR(2, "圆形"),
    ;
    private Integer value;
    private String desc;

    public Integer getValue() {
        return value;
    }

    @Override
    public Integer getDocument() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    EnumOverlayType(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }

    public static EnumOverlayType getByValue(Integer value) {
        if (null == value) {
            return null;
        }
        for (EnumOverlayType status : values()) {
            if (Objects.equals(status.getValue(), value)) {
                return status;
            }
        }
        return null;
    }
}
 ```
# EnumTradeInOrderTransactionProcessStatus
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumTradeInOrderTransactionProcessStatus implements DocumentedEnum<Integer> {
    PROCESSING(1, "处理中"),
    SUCCESS(2, "成功"),
    FAIL(3, "失败"),
    ;

    private final Integer document;
    private final String desc;

    EnumTradeInOrderTransactionProcessStatus(Integer document, String desc) {
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
# EnumRelativeOrderType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumRelativeOrderType implements DocumentedEnum<Integer> {
    /**
     * 延时保险
     */
    INSURANCE(1, "延保"),
    ;

    private final Integer document;
    private final String desc;

    EnumRelativeOrderType(Integer document, String desc) {
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
# EnumTradeInOrderPriceItemType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

/**
 * @author chujun
 */

public enum EnumTradeInOrderPriceItemType implements DocumentedEnum<Integer> {
    /**
     * 官网以旧换新补贴
     */
    OLD_OF_NEW_SUBSIDY(1, "以旧换新补贴"),
    /**
     * 应用端以旧换新补贴
     * (任然是爱回收本身提供的优惠，而非第三方的优惠)
     */
    AGENCY_SUBSIDY(2, "应用端以旧换新补贴"),
    ;
    private final Integer document;
    private final String desc;

    EnumTradeInOrderPriceItemType(Integer document, String desc) {
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
# EnumTradeInOrderGiftType
```
 package com.aihuishou.service.tic.model.enumerate;


import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumTradeInOrderGiftType implements DocumentedEnum<Integer> {
    RECYCLE_PROMOTION_PACKAGE(1, "回收券礼包");

    private final Integer document;
    private final String desc;

    EnumTradeInOrderGiftType(Integer document, String desc) {
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
# EnumTradeInOrderRefundStatus
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

import java.util.Objects;

public enum EnumTradeInOrderRefundStatus implements DocumentedEnum<Integer> {
    REFUNDING(1, "退款中"),
    REFUND_SUCCESS(2, "退款成功"),
    REFUND_EXCEPTION(3, "退款异常");

    private Integer value;
    private String desc;

    @Override
    public Integer getDocument() {
        return value;
    }

    public Integer getValue() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    EnumTradeInOrderRefundStatus(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }

    public static EnumTradeInOrderRefundStatus getByValue(Integer value) {
        if (null == value) {
            return null;
        }
        for (EnumTradeInOrderRefundStatus status : values()) {
            if (Objects.equals(status.getValue(), value)) {
                return status;
            }
        }
        return null;
    }


}
 ```
# InvoiceRequestCoralType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum InvoiceRequestCoralType implements DocumentedEnum<Integer> {
    TYPE_PERSONAL_ELECTRONIC_NORMAL(1, "个人电子增值税普通发票"),
    TYPE_COMPANY_ELECTRONIC_NORMAL(2, "公司电子增值税普通发票"),
    TYPE_PERSONAL_PAPER_NORMAL(3, "个人纸质增值税普通发票"),
    TYPE_COMPANY_PAPER_NORMAL(4, "公司纸质增值税普通发票"),
    TYPE_COMPANY_PAPER_SPECIAL(5, "公司纸质增值税专用发票");

    private final Integer document;
    private final String desc;

    InvoiceRequestCoralType(Integer document, String desc) {
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
# EnumTradeInOrderTraceOperation
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumTradeInOrderTraceOperation implements DocumentedEnum<Integer> {
    COOP_DELIVER(1, "合作方发货"),
    PAY(2, "支付"),
    CANCEL(3, "取消"),
    RECEIVE(4, "收货"),
    CONFIRM_ONDOOR(5, "确认上门信息"),
    DISPATCH(6, "派单"),
    STOCK_OUT(7, "出库"),
    OLD_ORDER_VALIDATE(8, "验货"),
    OLD_ORDER_SETTLE(9, "旧机结算"),
    SETTLE_START(10, "结算开始"),
    SETTLE_FINISH(11, "结算完成"),
    VERIFICATE(12, "核销"),
    APPLY_RETURN(13, "申请退货"),
    APPEND_APPLY_RETURN(14, "附加退货信息"),
    REFUND(15, "退款成功"),
    CREATE_ORDER(16, "创建订单"),
    MANUAL_ASSOCIATE_PACKAGE_EXPRESS(17, "关联包裹物流单号"),
    RETURN(18, "退货完成"),
    COOP_PAY(19, "合作方支付"),
    PRE_PAY(20, "预支付"),
    OLD_ORDER_FINAL(21, "旧机完结"),
    ;

    private final Integer document;
    private final String desc;

    EnumTradeInOrderTraceOperation(Integer document, String desc) {
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
# EnumTimelinessType
```
 package com.aihuishou.service.tic.model.enumerate;


import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumTimelinessType implements DocumentedEnum<Integer> {
    REALTIME(1, "实时"),
    APPOINTMENT(2, "履约时间"),
    ;
    private Integer value;
    private String desc;

    public Integer getValue() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    EnumTimelinessType(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }

    @Override
    public Integer getDocument() {
        return this.value;
    }
}
 ```
# EnumRecycleOrderStatusExtension
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

import java.util.Objects;
import java.util.Optional;

public enum EnumRecycleOrderStatusExtension implements DocumentedEnum<String> {
    TOBEVALIDATE("1", "待验货"),
    TOBEPAID("2", "待付款"),
    SUCCESS("3", "交易成功"),
    CANCEL("4", "已取消"),
    PAING("5", "支付中");

    private String document;
    private String desc;

    EnumRecycleOrderStatusExtension(String document, String desc) {
        this.document = document;
        this.desc = desc;
    }

    @Override
    public String getDocument() {
        return this.document;
    }

    @Override
    public String getDesc() {
        return this.desc;
    }

    public static Optional<EnumRecycleOrderStatusExtension> getByDocument(String value) {
        if (null == value) {
            return Optional.empty();
        }
        for (EnumRecycleOrderStatusExtension status : values()) {
            if (Objects.equals(status.getDocument(), value)) {
                return Optional.of(status);
            }
        }
        return Optional.empty();
    }
}

 ```
# EnumTradeInOrderTransactionScene
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

/**
 * 交易场景
 */
public enum EnumTradeInOrderTransactionScene implements DocumentedEnum<Integer> {
    SETTLE(0, "结算"),
    PRE_PAY(1, "预支付"),
    ;

    private final Integer document;
    private final String desc;

    @Override
    public Integer getDocument() {
        return document;
    }

    @Override
    public String getDesc() {
        return desc;
    }


    EnumTradeInOrderTransactionScene(Integer document, String desc) {
        this.document = document;
        this.desc = desc;
    }
}
 ```
# EnumOrderBusinessType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumOrderBusinessType implements DocumentedEnum<Integer> {
    RENEW(1, "换新"),
    SALE(2, "销售"),
    ;

    private Integer document;
    private String desc;

    EnumOrderBusinessType(Integer document, String desc) {
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
# EnumShopType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

import java.util.Objects;

/**
 * @author chujun
 * @see EnumShopV2Type
 */
@Deprecated
public enum EnumShopType implements DocumentedEnum<Integer> {
    OnlineShop(1, "线上门店"),
    Offline(2, "线下门店"),
    CoopMarket(3, "CoopMarket"),
    XiaomiShop(4, "小米门店"),
    JDShop(5, "京东门店"),
    OfflineLeagueShop(6, "线下加盟店"),
    ;
    private Integer value;
    private String desc;

    public Integer getValue() {
        return value;
    }

    @Override
    public Integer getDocument() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    EnumShopType(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }

    public static EnumShopType getByValue(Integer value) {
        if (null == value) {
            return null;
        }
        for (EnumShopType status : values()) {
            if (Objects.equals(status.getValue(), value)) {
                return status;
            }
        }
        return null;
    }
}
 ```
# EnumStationType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumStationType implements DocumentedEnum<Integer> {
    BIG(1, "大仓"),
    PRE(2, "前置仓"),
    ;
    private Integer value;
    private String desc;

    public Integer getValue() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    EnumStationType(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }

    @Override
    public Integer getDocument() {
        return this.value;
    }
}
 ```
# EnumTradeInOrderReceiptGatewayType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;
import io.swagger.annotations.ApiModel;

/**
 * @author chujun
 */

@ApiModel(description = "新机收款网管类型")
public enum EnumTradeInOrderReceiptGatewayType implements DocumentedEnum<Integer> {
    ALIPAY_BAR_CODE(1001, EnumTradeInOrderTransactionGatewayType.ALIPAY.getDocument(), "支付宝条码支付网关"),
    WECHAT_BAR_CODE(1002, EnumTradeInOrderTransactionGatewayType.WECHAT.getDocument(), "微信收款码支付网关"),
    ALIPAY_APP(1003, EnumTradeInOrderTransactionGatewayType.ALIPAY.getDocument(), "支付宝APP支付网关"),
    ALIPAY_PHONE_WEBSITE(1004, EnumTradeInOrderTransactionGatewayType.ALIPAY.getDocument(), "支付宝手机网站支付网关"),
    WECHAT_JSAPI(1005, EnumTradeInOrderTransactionGatewayType.WECHAT.getDocument(), "微信JSPAI支付网关"),
    WECHAT_APP(1006, EnumTradeInOrderTransactionGatewayType.WECHAT.getDocument(), "微信APP支付网关"),
    WECHAT_H5(1007, EnumTradeInOrderTransactionGatewayType.WECHAT.getDocument(), "微信H5支付网关"),
    WECHAT_MINI_PROGRAM(1008, EnumTradeInOrderTransactionGatewayType.WECHAT.getDocument(), "微信小程序支付网关"),
    ;

    private Integer document;
    private Integer transactionGatewayType;
    private String desc;

    EnumTradeInOrderReceiptGatewayType(Integer document, Integer transactionGatewayType, String desc) {
        this.document = document;
        this.transactionGatewayType = transactionGatewayType;
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

    public Integer getTransactionGatewayType() {
        return transactionGatewayType;
    }
}
 ```
# EnumBaseTradeInOrderPickupType
```
 package com.aihuishou.service.tic.model.enumerate;


import com.aihuishou.common.exception.ServiceException;
import com.aihuishou.common.model.constant.DocumentedEnum;

import java.util.Objects;

/**
 * @author chujun
 * @deprecated
 */
@Deprecated
public enum EnumBaseTradeInOrderPickupType implements DocumentedEnum<Integer> {
    DELIVER(4, "快递", 4),
    ONDOOR(1, "上门", 1),
    METRO(2, "地铁", 2),
    SHOP(5, "门店", 5),
    MTA(6, "MTA", 6),
    O2O_SHOP(7, "O2O门店", 5);

    private final Integer document;
    private final Integer recycleOrderPickupType;
    private final String desc;

    EnumBaseTradeInOrderPickupType(Integer document, String desc, Integer recycleOrderPickupType) {
        this.document = document;
        this.desc = desc;
        this.recycleOrderPickupType = recycleOrderPickupType;
    }

    @Override
    public Integer getDocument() {
        return document;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    /**
     * 旧机 EnumPickUpType
     */
    public Integer getRecycleOrderPickupType() {
        return recycleOrderPickupType;
    }

    /**
     * TODO:cj 后续删除
     * 供上游使用
     */
    public static Integer convertToCoralOrderPickupType(Integer pickupType) {
        if (null == pickupType) {
            throw ServiceException.ofMessage("无法转化订单取货方式,pickupType=" + pickupType);
        }
        if (Objects.equals(EnumGenericPickupType.SHOP.getDocument(), pickupType)) {
            return EnumTradeInOrderPickupType.SHOP.getValue();
        } else if (Objects.equals(EnumGenericPickupType.O2O_SHOP.getDocument(), pickupType)) {
            return EnumTradeInOrderPickupType.O2O_SHOP.getValue();
        } else if (Objects.equals(EnumGenericPickupType.ONDOOR.getDocument(), pickupType)) {
            return EnumTradeInOrderPickupType.ON_DOOR.getValue();
        }
        throw ServiceException.ofMessage("无法转化订单取货方式,pickupType=" + pickupType);
    }
}
 ```
# EnumProductSource
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;
import com.google.common.collect.Lists;

import java.util.List;

public enum EnumProductSource implements DocumentedEnum<Integer> {
    AHS(0, Lists.newArrayList(0), "爱回收"),
    SAMSUNG(1, Lists.newArrayList(EnumCoopOrderType.SAMSUNG.getDocument()), "三星"),
    FEN_QI_LE(2, Lists.newArrayList(EnumCoopOrderType.FEN_QI_LE.getDocument(), EnumCoopOrderType.SHARE_FEN_QI_LE.getDocument()), "分期乐"),
    JD_ONE_STOP(3, Lists.newArrayList(EnumCoopOrderType.JD_ONE_STOP.getDocument()), "京东一站式"),
    HUA_WEI(4, Lists.newArrayList(EnumCoopOrderType.HUA_WEI.getDocument()), "华为"),
    ;

    private final Integer document;
    private final String desc;
    private final List<Integer> coopOrderTypes;

    EnumProductSource(Integer document, List<Integer> coopOrderTypes, String desc) {
        this.document = document;
        this.desc = desc;
        this.coopOrderTypes = coopOrderTypes;
    }

    @Override
    public Integer getDocument() {
        return document;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    public List<Integer> getCoopOrderTypes() {
        return coopOrderTypes;
    }

    public static EnumProductSource getByCoopOrderType(Integer coopOrderType) {
        if (null == coopOrderType) {
            return EnumProductSource.AHS;
        }
        for (EnumProductSource item : values()) {
            if (item.getCoopOrderTypes().contains(coopOrderType)) {
                return item;
            }
        }
        return EnumProductSource.AHS;
    }
}
 ```
# EnumScanType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumScanType implements DocumentedEnum<Integer> {
    NO_NEED_SCAN(0, "无需扫码"),
    IMEI(1, "imei"),
    EXPRESS_NO(2, "快递单号"),
    ;

    private final Integer document;
    private final String desc;

    EnumScanType(Integer document, String desc) {
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
# EnumTradeInOrderDiscountType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

import java.util.Objects;

public enum EnumTradeInOrderDiscountType implements DocumentedEnum<Integer> {
    OFNEW_SUBSIDY(1, "以旧换新补贴"),
    OFNEW_BARGAIN(2, "以旧换新砍价"),
    COUPON(3, "新机优惠券"),
    //TODO:cj to be done
    PRICE_INCREASE_ACTIVITY(4, "加价购");

    private Integer value;
    private String desc;

    public Integer getValue() {
        return value;
    }

    @Override
    public Integer getDocument() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    EnumTradeInOrderDiscountType(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }

    public static EnumTradeInOrderDiscountType getByValue(Integer value) {
        for (EnumTradeInOrderDiscountType discountType : values()) {
            if (Objects.equals(discountType.getValue(), value)) {
                return discountType;
            }
        }
        return null;
    }
}
 ```
# EnumSubsidyType
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumSubsidyType implements DocumentedEnum<Integer> {
    ABSOLUTE_DISCOUNT(1, "绝对值折扣"),
    RECYCLE_COUPON(2, "回收加价券");

    private Integer value;
    private String desc;

    public Integer getValue() {
        return value;
    }

    @Override
    public Integer getDocument() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    EnumSubsidyType(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }
}
 ```
# EnumProductImportanceType
```
 package com.aihuishou.service.tic.model.enumerate;


import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumProductImportanceType implements DocumentedEnum<Integer> {
    MAIN(1, "主品"),
    GIFT(2, "赠品"),
    ;
    private Integer value;
    private String desc;

    public Integer getValue() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    EnumProductImportanceType(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }

    @Override
    public Integer getDocument() {
        return this.value;
    }
}
 ```
# EnumInvoiceGenre
```
 package com.aihuishou.service.tic.model.enumerate;

public enum EnumInvoiceGenre {
    PERSONAL_ELECTRONIC_NORMAL(
        "个人电子增值税普通发票"
    ),
    PERSONAL_PAPER_NORMAL(
        "个人纸质增值税普通发票"
    ),
    ENTERPRISE_ELECTRONIC_NORMAL(
        "公司电子增值税普通发票"
    ),
    ENTERPRISE_PAPER_NORMAL(
        "公司纸质增值税普通发票"
    ),
    ENTERPRISE_PAPER_SPECIAL(
        "公司纸质增值税专用发票"
    ),
    ;

    private final String desc;

    EnumInvoiceGenre(String desc) {
        this.desc = desc;
    }

    public String getDesc() {
        return desc;
    }
}
 ```
# EnumCoopPackageStatus
```
 package com.aihuishou.service.tic.model.enumerate;


import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumCoopPackageStatus implements DocumentedEnum<Integer> {
    PACKAGING(1, "待发货"),
    DELIVERING(2, "配送中"),
    RECEIVED(3, "已收货"),
    DELIVERED(4, "已妥投"),
    REJECTED(5, "已拒收"),
    ;

    private final Integer document;
    private final String desc;

    EnumCoopPackageStatus(Integer document, String desc) {
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
# EnumPackageProductType
```
 package com.aihuishou.service.tic.model.enumerate;


import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumPackageProductType implements DocumentedEnum<Integer> {
    REALITY(1, "实物"),
    VIRTUAL(2, "虚拟"),
    ;
    private Integer value;
    private String desc;

    public Integer getValue() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    EnumPackageProductType(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }

    @Override
    public Integer getDocument() {
        return this.value;
    }
}
 ```
# EnumTradeInOrderPayStatus
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

import java.util.Objects;

public enum EnumTradeInOrderPayStatus implements DocumentedEnum<Integer> {
    PAYING(1, "支付中"),
    PAY_SUCCESS(2, "支付成功"),
    PAY_EXCEPTION(3, "支付失败");

    private Integer value;
    private String desc;

    public Integer getValue() {
        return value;
    }

    @Override
    public Integer getDocument() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    EnumTradeInOrderPayStatus(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }

    public static EnumTradeInOrderPayStatus getByValue(Integer value) {
        if (null == value) {
            return null;
        }
        for (EnumTradeInOrderPayStatus status : values()) {
            if (Objects.equals(status.getValue(), value)) {
                return status;
            }
        }
        return null;
    }
}
 ```
# EnumTradeInOrderStatus
```
 package com.aihuishou.service.tic.model.enumerate;

import java.util.Objects;

/**
 * @deprecated
 */
@Deprecated
public enum EnumTradeInOrderStatus {
    PENDING(1, "待付款"),
    PAID(2, "已付款"),
    COMPLETED(3, "已完成"),
    CANCELLED(4, "已取消"),
    REFUNDED(5, "已退款"),
    RECYCLE_INSPECT_PENDING(31, "待核验"),
    STATUS_CONFIRM_PENDING(6, "待确认");

    private Integer value;
    private String desc;

    public Integer getValue() {
        return value;
    }

    public String getDesc() {
        return desc;
    }

    EnumTradeInOrderStatus(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }

    public static EnumTradeInOrderStatus getByValue(Integer value) {
        for (EnumTradeInOrderStatus status : values()) {
            if (Objects.equals(status.getValue(), value)) {
                return status;
            }
        }
        return null;
    }
}
 ```
# EnumTradeInCoopPackageTraceOperation
```
 package com.aihuishou.service.tic.model.enumerate;


import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumTradeInCoopPackageTraceOperation implements DocumentedEnum<Integer> {
    DELIVER(1, "发货"),
    RECEIVE(2, "收货"),
    DELIVERED(3, "妥投"),
    REJECT(4, "拒收"),
    UPDATE(5, "更新"),
    CANCEL(6, "取消"),
    COMPENSATE_DELIVERY(7, "补偿物流单号"),
    ;

    private final Integer document;
    private final String desc;

    EnumTradeInCoopPackageTraceOperation(Integer document, String desc) {
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
}
 ```
# EnumTradeInOrderGiftCouponDiscardStatus
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumTradeInOrderGiftCouponDiscardStatus implements DocumentedEnum<Integer> {
    INIT(0, "初始状态"),
    DISCARDED(1, "已作废"),
    DISCARD_FAILED(2, "无法作废"),
    ;
    private final Integer document;
    private final String desc;

    EnumTradeInOrderGiftCouponDiscardStatus(Integer document, String desc) {
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
# EnumTradeInOrderPickupType
```
 package com.aihuishou.service.tic.model.enumerate;

import java.util.Objects;

/**
 * @deprecated
 */
@Deprecated
public enum EnumTradeInOrderPickupType {
    SF_EXPRESS(1, "顺丰"),
    STAFF(2, "员工送货"),
    SHOP(3, "门店"),
    ON_DOOR(4, "上门"),
    O2O_SHOP(5, "O2O门店");

    private Integer value;
    private String desc;

    public String getDesc() {
        return desc;
    }

    public Integer getValue() {
        return value;
    }

    EnumTradeInOrderPickupType(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }

    public static EnumTradeInOrderPickupType getByValue(Integer value) {
        for (EnumTradeInOrderPickupType pickupType : values()) {
            if (Objects.equals(pickupType.getValue(), value)) {
                return pickupType;
            }
        }
        return null;
    }
}
 ```
# EnumSubsidyScene
```
 package com.aihuishou.service.tic.model.enumerate;

import com.aihuishou.common.model.constant.DocumentedEnum;

public enum EnumSubsidyScene implements DocumentedEnum<Integer> {
    SELL_ONLY(1, "仅售卖新机"),
    RECYCLE_AND_SELL(2, "以旧换新");

    private Integer value;
    private String desc;

    public Integer getValue() {
        return value;
    }

    @Override
    public Integer getDocument() {
        return value;
    }

    @Override
    public String getDesc() {
        return desc;
    }

    EnumSubsidyScene(Integer value, String desc) {
        this.value = value;
        this.desc = desc;
    }
}
 ```
