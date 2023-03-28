export type StaticThis<T> = { new (args: any): T };

/**
 * @description является корневым прототипом для классов auth
 */
export class BaseObject {
  //noinspection JSUnusedLocalSymbols
  constructor(args: {}) {}

  /**
   * @description скрывает детали создания экземпляра любого класса, который наследует данный BaseObject
   */
  static make<T extends BaseObject>(this: StaticThis<T>, args: any = null) {
    return new this(args);
  }
}
