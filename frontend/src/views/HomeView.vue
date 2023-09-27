<script setup lang="ts">
import { Ref, ref } from 'vue';
import TheWelcome from '../components/TheWelcome.vue'
import RemoteService from '@/services/RemoteServices'

const hello: Ref<String> = ref('');

teste();
async function teste(){
  await RemoteService.getHello().then((response) => {
    console.log(response);  
      hello.value = response;
    })
    console.log(hello.value);
};

</script>

<template>
  <main>
    <h1>Home2 {{ hello }}</h1>
    <TheWelcome />
  </main>
</template>
