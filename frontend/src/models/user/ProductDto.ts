export default class ProductDto {
    product_type?: string;
    product_url?: string;
    actual_value?: number;
    product_buyer?: string;
    closed?: boolean;
    product_id?: number;
    client_username?: string;


    // "product_id": 1,
    // "client_username": 2,
    // "product_type": "camisa",
    // "actual_value": 200,
    // "product_buyer": "zeric",
    // "product_url": "models.CharField(max_length=100)",
    // "closed": false
    
    constructor(jsonObj: Partial<ProductDto>) {
      Object.assign(this, jsonObj);
    }
  }
  