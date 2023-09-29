import axios from 'axios';
import type { AxiosResponse } from 'axios';
import UserDto from '@/models/user/UserDto';
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

    // create a function that sent a json with user and password to the backend
    static async registerUser(user: UserDto): Promise<String> {
      return httpClient.post('/api/createClient/', user).then((response: AxiosResponse) => {
        console.log(response.data);
        // return sucess if status is 200 and error if status is different
        return response.data;
      });
    }

    static async login(user: UserDto): Promise<String> {
      return httpClient.post('/api/login/',user).then((response: AxiosResponse) => {
        console.log(response);
        return response;
      });
    }
    static async logout(): Promise<String>{
      return httpClient.get('/api/logout').then((response: AxiosResponde) =>{
        console.log(response.data);
        return response.data;
      });
    }

    static async createProduct(product: ProductDto): Promise<String>{
      return httpClient.post('/api/createAuctionProducts/',product).then((response: AxiosResponse) => {
        console.log(response.data);
        return response.data;
      });
    }

    static async addBalance(value: int): Promise<String>{
      let balance = {"value": value}
      return httpClient.post('/api/addBallance/',balance).then((response: AxiosResponse) => {
        console.log(response.data);
        return response.data;
      });
    }

    static async showAuctionProducts(): Promise<String[]>{
      return httpClient.post('/api/showAuctionProducts/').then((response: AxiosResponse) => {
        console.log(response.data);
        return response.data;
      });
    }

    static async AuctionClientProducts(): Promise<String[]>{
      return httpClient.post('/api/clientAuctionProducts/').then((response: AxiosResponse) => {
        console.log(response.data);
        return response.data;
      });
    }

    static async AuctionProduct(value: int,product_id: int ): Promise<String[]>{
      let auctionvalue = {"value": value ,"product_id":product_id}
      return httpClient.post('/api/auctionProduct/',auctionvalue).then((response: AxiosResponse) => {
        console.log(response.data);
        return response.data;
      });
    }

    
    static async CloseAuctionProducts(product_id: int): Promise<String[]>{
      let close = {"product_id":product_id}
      return httpClient.post('/api/closeAuctionProducts/',close).then((response: AxiosResponse) => {
        console.log(response.data);
        return response.data;
      });
    }

}

    