<template>
	
	<v-card class="pt-5 px-10 pb-5">
		<v-row class="mb-2">
			<v-col>
				<h2 class="text-center">Registar Usuário</h2>
			</v-col>
		</v-row>

    <v-form>
      <v-row>
        <v-col>
          <v-text-field label="Username" required prepend-icon="fas fa-user"></v-text-field>
        </v-col>
			</v-row>
			<v-row>
        <v-col>
          <v-text-field label="Password" required prepend-icon="fas fa-envelope"></v-text-field>
        </v-col>
      </v-row>
			<v-btn color="primary" @click="submit" >
        Registar
      </v-btn>
    </v-form>
  </v-card>
</template>

<script setup lang="ts">
import { type Ref, ref } from 'vue'
import RemoteService from '@/services/RemoteServices'
import { UserDto } from '@/types/UserDto'

async function submit() {
	const user: UserDto = {
		client_username: "teste",
		client_password: "passwordTeste",
	};

	await RemoteService.registerUser(user).then((response) => {
		console.log(response)
	})
}
</script>
