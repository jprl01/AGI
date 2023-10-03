<template>
  <nav>
    <v-app-bar style="height: 60px; top: 0px">
      <v-toolbar title="AGI-Auction">
        <v-toolbar-items>
          
          <v-btn  to="/">Auctios</v-btn>
          <!-- create a button to call the api HelloWorld -->
          <v-btn to="/hello">My Auctions</v-btn>
          <v-btn to="/hello">My Auctions</v-btn>
          
          <v-btn v-if="!store.isLoggedIn" to="/login">Login</v-btn>
          <v-btn to="/register">Register</v-btn>
          <v-btn v-if="store.isLoggedIn" @click="logout">Logout</v-btn>
          <v-btn v-if="store.isLoggedIn" to="/profile">Profile</v-btn>

        </v-toolbar-items>
      </v-toolbar>
    </v-app-bar>
  </nav>
</template>
<script setup lang="ts">
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'

import { useAuthStore } from '@/stores/counter'

const store = useAuthStore();

function logout(){
  store.logout();

}
</script>
