import { Quasar } from 'quasar';
import quasarUserOptions from './quasar-user-options';
import router from "./router";
import store from './store';
import {Component, createApp} from "vue";


export default (App: Component) => {
    return createApp(App).use(store).use(Quasar, quasarUserOptions).use(router).use(Quasar, quasarUserOptions)
}