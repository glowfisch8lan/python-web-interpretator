import {BaseObject} from "@/core/base/BaseObject";

/**
 * @description DTO - структура, которая гаран  тирует наличие конкретных полей и данных в системе
 * @class AuthResultDto
 */
export class MenuItemDto extends BaseObject {

    public id: number;
    public routeName: string;

    /**
     * @param args
     */
    constructor(args: {id: number, routeName: string}) {
        super(args);
        this.id = args.id;
        this.routeName = args.routeName;
    }
}
