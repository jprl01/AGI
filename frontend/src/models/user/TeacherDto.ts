export default class TeacherDto {
  username?: string;
  name?: string;
  email?: string;
  registrationDate!: string; // yyyy-mm-dd HH:MM

  constructor(jsonObj: Partial<TeacherDto>) {
    Object.assign(this, jsonObj);
  }
}
