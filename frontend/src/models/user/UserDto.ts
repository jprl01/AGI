export default class UserDto {
  client_id?: number;
  client_username?: string;
  balance?: number;
  virtual_balance?: number;


  constructor(jsonObj: Partial<UserDto>) {
    Object.assign(this, jsonObj);
  }
}
