import axios from 'axios';
import type { AxiosResponse } from 'axios';

const httpClient = axios.create();
httpClient.defaults.timeout = 50000;
httpClient.defaults.baseURL = import.meta.env.VITE_ROOT_API;
httpClient.defaults.headers.post['Content-Type'] = 'application/json';
httpClient.interceptors.request.use(
  // TODO: don't send token for ALL requests, filter by target host
  // only send to backend-bound requests

  (config) => {
    // if (!config.headers.Authorization) {
    //   const token = useAuthStore().token;
    //   if (token) {
    //     config.headers.Authorization = `Bearer ${token}`;
    //   }
    // }

    return config;
  },
  (error: any) => Promise.reject(error)
);

export default class RemoteServices {

  
    static async getHello(): Promise<String> {
        console.log("getHello");
      return httpClient.get('/api/hello').then(() => {
        return "Hello World";
      });
    }
}