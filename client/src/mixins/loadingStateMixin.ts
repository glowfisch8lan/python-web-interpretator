// @ts-ignore
export default {
    methods: {
        showLoading(text: string = ''): void {
            // @ts-ignore
            this.$q?.loading.show({
                message: text ?? 'Идет загрузка приложения...'
            })
        },
        hideLoading(): void {
            console.log('Hide loading')
            // @ts-ignore
            this.$q?.loading.hide()
        }
    },
    computed: {
        loading: {
            set: function (value: boolean): void {
                // @ts-ignore
                this.$store.state.loading = value
            },
            get: function (): any {
                // @ts-ignore
                return this.$store.state.loading
            }
        },
    },
}