import UserDto from '@/models/user/UserDto';

export default class AuthDto {
  token?: string;
  user?: UserDto;

  constructor(jsonObj: Partial<AuthDto>) {
    Object.assign(this, jsonObj);
    if (jsonObj.user) {
      this.user = new UserDto(jsonObj.user);
    }
  }
}
