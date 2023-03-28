import App from './App.vue'
import bootstrap from "./bootstrap";

export default function placeApp(el: any) {
  bootstrap(App).mount(el);
}
