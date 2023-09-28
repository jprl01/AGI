export default class ProductDto {
    product_type?: string;
    product_url?: string;
    actual_value?: int;

    constructor(jsonObj: Partial<UserDto>) {
      Object.assign(this, jsonObj);
    }
  }
  