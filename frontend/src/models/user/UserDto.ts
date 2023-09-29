export default class UserDto {
  username?: string;
  password?: string;

  constructor(jsonObj: Partial<UserDto>) {
    Object.assign(this, jsonObj);
  }
}
