<template>
  <v-card class="pt-5 px-10 pb-5">
    <v-row class="mb-2">
      <v-col>
        <h2 class="text-center">Registar Usuário</h2>
      </v-col>
    </v-row>

    <v-form v-model="valid" ref="form">
      <v-row>
        <v-col>
          <v-text-field
            v-model="username"
            label="Username"
						:rules="usernameRule"
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
						:rules="passwordRule"
						clearable
            prepend-icon="fas fa-envelope"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-btn color="primary" :disabled="!valid" @click="submit"> Registar </v-btn>
    </v-form>
  </v-card>
</template>

<script setup lang="ts">
import { type Ref, ref, reactive } from 'vue'
import RemoteService from '@/services/RemoteServices'
import { UserDto } from '@/types/UserDto'
import type { VForm } from 'vuetify/components';
import router from '@/router';

const form = ref<InstanceType<typeof VForm>>();
const valid = ref(false)
const username = ref('')
const password = ref('')

const usernameRule = reactive([
  (v: string) => !!v || 'O username é obrigatório',
]);

const passwordRule = reactive([
  (v: string) => !!v || 'A password é obrigatória',
]);

async function submit() {
  const user: UserDto = {
    "username": username.value,
    "password1": password.value,
    "password2": password.value
  }

  await RemoteService.registerUser(user).then((response) => {
    console.log(response)
		router.push({ path: '/login'})
		form.value?.reset();
  })
}
</script>
