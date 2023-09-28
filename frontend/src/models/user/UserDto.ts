export default class UserDto {
  client_username?: string;
  client_password?: string;

  constructor(jsonObj: Partial<UserDto>) {
    Object.assign(this, jsonObj);
  }
}
