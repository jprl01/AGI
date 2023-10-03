<template>
  <div>
    <v-row class="mb-2">
      <v-data-table :headers="headers" :items="products" class="text-left">
        <template v-slot:item.actions="{ item }">
          <div class="d-flex flex-wrap justify-center align-center">
            <v-btn
              color="error"
            >
              Fechar
            </v-btn>
          </div>
        </template>
      </v-data-table>
    </v-row>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '@/stores/counter'
import { computed, ComputedRef, reactive, ref, Ref } from 'vue'
import RemoteService from '@/services/RemoteServices'
//import ProductDto
import type ProductDto from '@/models/user/ProductDto'
import { VDataTable } from 'vuetify/labs/VDataTable'

const headers: ComputedRef<
  {
    title: string
    key: string
    [k: string]: unknown
  }[]
> = computed(() => [
  {
    title: 'Identificador',
    key: 'product_id',
    align: 'start'
  },
  {
    title: 'actual_price',
    key: 'actual_value',
    align: 'start'
  },
  {
    title: 'buyer',
    key: 'product_buyer',
    align: 'start'
  },
  {
    title: 'closed',
    key: 'closed',
    align: 'start'
  },
  {
    title: 'url',
    key: 'product_url',
    align: 'start'
  },
  {
    title: 'Ações',
    key: 'actions',
    align: 'center',
    searchable: false,
    sortable: false
  }
])

const store = useAuthStore()
const products: Ref<ProductDto[]> = ref([])
const loading = ref(true)

getClientAuction()
console.log('passa')

async function getClientAuction() {
  await RemoteService.getClientAuction().then((values) => {
    products.value = values
    console.log(products)
    loading.value = false
  })
}
</script>
