<template>
  <q-page-container>
    <div class="q-pt-xs">
      <h4 style="text-align:center;">Python</h4>
      <div class="container">
        <div class="row">
          <div class="col-6">
            <div class="q-pa-md" style="width:100%">
              <q-input
                  v-model="code"
                  filled
                  dark
                  bg-color="black"
                  label="Выполняемый код"
                  label-color="white"
                  type="textarea"
              />
            </div>
          </div>

          <div class="col-6">
            <div class="q-pa-md" style="width:100%;">
              <q-input
                  readonly
                  v-model="output"
                  filled
                  label="Вывод:"
                  type="textarea"
              />
            </div>
          </div>
        </div>
        <div class="col-md-12 text-center">
          <q-btn color="primary" type="submit" class="btn btn-primary" @click="submit">Выполнить</q-btn>
        </div>

        <div style="width:100%" class="fit row wrap justify-center items-start content-start">
          <q-img width="720px" v-for="img in imgs" :src="getImageUrl(img)" position="center"/>
        </div>
      </div>
    </div>
  </q-page-container>
</template>

<script lang="ts">
import {defineComponent} from "vue";
import NavigationMenu from "../components/NavigationMenu.vue";
import loadingStateMixin from "@/mixins/loadingStateMixin";
import axios from "axios";

export default defineComponent({
  name: 'MainPage',
  mixins: [loadingStateMixin],
  components: {NavigationMenu},
  methods: {
    getImageUrl(img: string) {
      return "/api/v1/get_img/" + img;
    },
    submit() {
      this.showLoading('Идет обработка...')
      axios({
        method: 'post',
        url: '/api/v1/run-code',
        data: this.code,
        headers: {
          'content-type': 'raw'
        }
      }).then((result: any) => {
        console.log(result.data)
        this.output = result.data.data.result
        this.imgs = result.data.data.imgs
      }).catch((err: any) => this.$q.notify({
        type: 'negative',
        message: 'Что-то пошло не так... => ' + err
      })).finally(() => this.hideLoading())
    }
  },
  data() {
    return {
      output: '',
      code: "",
      imgs: []
    }
  },
});
</script>

<style>
textarea {
  height: 480px
}
</style>