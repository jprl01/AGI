<template>
  <div>
    <v-row class="mb-2">
      <v-col>
        <h2 class="text-left">Profile info  </h2>
      </v-col>
      <v-col cols="auto">
        <v-btn color="info" @click="showDialog = true" class="mt-3 mt-sm-0"> Add Balance </v-btn>
      </v-col>
    </v-row>
    <v-form v-if="!loading">

      <v-row>
        <v-col>
          <v-text-field
            v-model="username"
            label="Nome Completo"
            :disabled="true"
            prepend-icon="fas fa-user"
          ></v-text-field>
          </v-col>
          <v-col>
          <v-text-field
            v-model="user.balance"
            label="Balance"
            :disabled="true"
            prepend-icon="fas fa-user"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            v-model="user.virtual_balance"
            label="Virtual Balance"
            :disabled="true"
            prepend-icon="fas fa-user"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-form>
    <v-dialog v-model="showDialog" width="auto">
    <v-card class="px-5 pt-5">
      <v-card-title>Add Balance</v-card-title>
      <v-card-text>
        <v-form v-model="valid" ref="form">
          <v-row>
            <v-text-field
              v-model="newBalance"
              label="Balance"
              required
              autofocus
              :rules="typeRules"
            />
          </v-row>
          <v-card-actions>
        <v-spacer />
        <v-btn
          color="error"
          data-cy="cancelButton"
          @click="
            showDialog = false;
            form?.reset();
          "
        >
          Cancel
        </v-btn>
        <v-btn
          :disabled="!valid"
          color="success"
          @click="incrementBalance"
        >
          Add
        </v-btn>
      </v-card-actions>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup lang="ts">

//import store
import { useAuthStore } from '@/stores/counter'
import { reactive, Ref, ref } from 'vue';
import RemoteServices from '@/services/RemoteServices';
import type UserDto from '@/models/user/UserDto';
import { VForm } from 'vuetify/lib/components/index.mjs';

const store = useAuthStore();
const username = ref('');
const user: Ref<UserDto | null> = ref(null);
const loading = ref(true);
const showDialog = ref(false);
const valid = ref(false);

const form = ref<InstanceType<typeof VForm>>();
const newBalance = ref('');
username.value = store.authUser.username;



const typeRules = reactive([
  (v: string) => ( !!v && parseInt(v) > 0 ) || 'Tem de ser um inteiro positivo',
]);

loadUser();

async function loadUser() {
  await RemoteServices.getClient().then((response) => {
    user.value = response;
    console.log(user.value);
    loading.value = false;
    console.log(loading.value);
  });
}

async function incrementBalance(){
  
  await RemoteServices.addBalance(parseInt(newBalance.value)).then(() => {
  
    showDialog.value = false;
    form.value?.reset();
    loadUser();
  });
}

</script>
