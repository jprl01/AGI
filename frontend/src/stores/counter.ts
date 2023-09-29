import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import type UserDto from '@/models/user/UserDto';
import RemoteServices from '@/services/RemoteServices';

export const useAuthStore = defineStore('auth', {
  persist: true,
  state: () => ({
    user: null as UserDto | null,
    token: '',
    isLoggedIn: false,
  }),
  getters: {
    getUser(): UserDto | null {
      return this.user;
    },
    getToken(): string {
      return this.token;
    },
    getIsLoggedIn(): boolean {
      return this.isLoggedIn;
    },
  },  
  actions: {
    async login(user: UserDto) {
      console.log("login");
      await RemoteServices.login(user).then((response) => {
        
        if(response['status'] == 201){
          console.log(response['status']);
          
          this.user = user;
          this.isLoggedIn = true;
          
        }
      });
      // console.log(authResponse);
    }
  },

});
