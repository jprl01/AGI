<template>
  <div>
    <v-row class="mb-2">
      <v-col>
        <h2 class="text-left">Listagem de Materiais</h2>
      </v-col>
      <v-col cols="auto">
        <v-btn color="info" data-cy="createMaterial" class="mt-3 mt-sm-0"> Adicionar Material </v-btn>
      </v-col>
    </v-row> 
    
    <v-card class="elevation-4 pa-6">
      <v-card-title class="text-h5">Hello World</v-card-title>
      <v-card-text>
        <p>{{ hello }}</p>
      </v-card-text>
    </v-card>
  </div>
</template>

<script setup lang="ts">
import RemoteService from '@/services/RemoteServices'
import { type Ref, ref } from 'vue'

const hello = ref('')

teste()
async function teste() {
  await RemoteService.getHello().then((response) => {
    hello.value = response
  })
}

</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
