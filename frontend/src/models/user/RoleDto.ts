export default class RoleDto {
  name?: string;
  description?: string;

  constructor(jsonObj: Partial<RoleDto>) {
    Object.assign(this, jsonObj);
  }
}
