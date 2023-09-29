export default class StudentDto {
  username?: string;
  name?: string;
  email?: string;
  registrationDate?: string; // yyyy-mm-dd HH:MM
  completedEcts?: number;
  campus?: 'ALAMEDA' | 'TAGUSPARK' | 'TODOS';
  forgotLastAssignment?: boolean;
  authorized?: boolean;

  constructor(jsonObj: Partial<StudentDto>) {
    Object.assign(this, jsonObj);
  }
}
