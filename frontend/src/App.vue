<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import TopBar from '@/components/TopBar.vue'
</script>

<template>
  <v-app id="app">
    <TopBar />
    <div
      style="margin-top: 36px"
      class="pa-10 d-flex flex-column flex-grow-1 flex-shrink-1 text-center"
    >
        <v-card class="elevation-4 pa-6">
        <router-view />
      </v-card>
    </div>

  </v-app>
</template>

<script setup lang="ts"></script>
