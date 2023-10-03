import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import type UserDto from '@/models/user/UserDto';
import RemoteServices from '@/services/RemoteServices';

export const useAuthStore = defineStore('auth', {
  persist: true,
  state: () => ({
    accessToken: '',
    refreshToken: '',
    authUser: null,
    isLoggedIn: false,
  }),
  getters: {
    getUser(): UserDto | null {
      return this.authUser;
    },
    getAccessToken(): string {
      return this.accessToken;
    },
    getIsLoggedIn(): boolean {
      return this.isLoggedIn;
    },
  },  
  actions: {
    async login(user: UserDto) {
      await RemoteServices.login(user).then((response) => {
        console.log(response)
        this.authUser = response.data.user;
        this.accessToken = response.data["access_token"];
        this.refreshToken = response.data["refresh_token"];
        this.isLoggedIn = true;
      });
      // console.log(authResponse);
    },
    async logout() {
      if (this.isLoggedIn) {
          this.authUser = null;
          this.accessToken = '';
          this.refreshToken = '';
          this.isLoggedIn = false;
      }
    }
  },
  // userLogin (context, usercredentials) {
  //   return new Promise((resolve, reject) => {
  //     axios.post('/api/clients/login/', {
  //       "username": usercredentials.username,
  //       "password": usercredentials.password
  //     },{ withCredentials: true })
  //     .then(response => {
  //       context.commit("setAuthUser", response.data.user);
  //       console.log(response.data)
  //       context.commit('updateStorage', { access: response.data["access_token"], refresh: response.data["refresh_token"] }) 
  //       // context.commit("serUsername", usercredentials.username);
  //       resolve()
  //     })
  //     .catch(err => {
  //       reject(err)
  //     })
  // })
  // }

});
