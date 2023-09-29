<template>
  <v-card class="pt-5 px-10 pb-5">
    <v-row class="mb-2">
      <v-col>
        <h2 class="text-center">Login</h2>
      </v-col>
    </v-row>

    <v-form v-model="valid" ref="form">
      <v-row>
        <v-col>
          <v-text-field
            v-model="username"
            label="Username"
            required
            prepend-icon="fas fa-user"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-text-field
            v-model="password"
            label="Password"
            required
            clearable
            prepend-icon="fas fa-envelope"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-btn color="primary" :disabled="!valid" @click="submit"> Login </v-btn>
    </v-form>
  </v-card>
</template>

<script setup lang="ts">
import { type Ref, ref, reactive } from 'vue'
import RemoteService from '@/services/RemoteServices'
import { UserDto } from '@/types/UserDto'
import type { VForm } from 'vuetify/components'
import router from '@/router';

//import store
import { useAuthStore } from '@/stores/counter'

const store = useAuthStore();
console.log(store)
const form = ref<InstanceType<typeof VForm>>()
const valid = ref(false)
const username = ref('')
const password = ref('')



async function submit() {

  const user: UserDto = {
    username: username.value,
    password: password.value
  }


  store.login(user);
  router.push({ path: '/'})

//   store.login(user);

//   await RemoteService.login(user).then((response) => {
//     console.log(response)
//     form.value?.reset()
//     router.push({ path: '/' })
//   })
}

console.log(store.user?.client_username);
</script>
