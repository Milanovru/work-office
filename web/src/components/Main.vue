<template>
    <main>
        <select name="forms" :selected="true" v-model="selected">
            <option v-for="form in forms" :key="form">{{form}}</option>
        </select>
        <Document :header="renderHeader" :footer="renderFooter" :date="renderDate" />
    </main>
</template>

<script>
import Document from './Document.vue'
import axios from 'axios'

export default {
    data() {
        return {
            selected: "formtest.docx",
            forms: null,
            headers: {
                ndd: "<p>Начальнику 13 отдела УИТО Спецсвязи ФСО России<br /><br />полковнику Насакину Д.Д.</p>",
                gav: "<p>Заместителю начальника отдела – начальнику 2 отделения 13 отдела УИТО Спецсвязи ФСО России<br ><br />полковнику Горжанову А.В.</p>"
            },
            footers: {
                ndd: ["<p>Начальник 13 отдела УИТО<br />Спецсвязи ФСО России<br />полковник<br /></p>", "Д.Д. Насакин"],
                gav: ["<p>Заместитель начальника отдела –<br />начальник 2 отделения 13 отдела<br />УИТО Спецсвязи ФСО России<br />полковник<br /></p>", "А.В. Горжанов"]
            },
            date: {},
        }
    },
    methods: {
        moderateMonth(month) {
            switch (month) {
                case 0:
                    return "января";
                case 1:
                    return "февраля";
                case 2:
                    return "марта";    
                case 3:
                    return "апреля";
                case 4:
                    return "мая";
                case 5:
                    return "июня";
                case 6:
                    return "июля";
                case 7:
                    return "августа";
                case 8:
                    return "сентября";
                case 9:
                    return "октрября";
                case 10:
                    return "ноября";
                case 11:
                    return "декабря";           
                default:
                    return "дата не определена"
            }
        },
    },
    components: {
        Document
    },
    computed: {
        renderHeader() {
            if (this.selected == 'formtest.docx') {
                return this.headers.gav
            } else if (this.selected == 'formtest2.docx') {
                return this.headers.ndd
            }
        },
        renderFooter() {
            if (this.selected == 'formtest.docx') {
                return this.footers.gav
            } else if (this.selected == 'formtest2.docx') {
                return this.footers.ndd
            }
        },
        renderDate() {
            let now = new Date()
            let currentYear = now.getFullYear()
            let currentMonth = now.getMonth()  // начинается с 0
            let currentDay = now.getDate()
            let currentDate = {
                year: currentYear, 
                month: this.moderateMonth(currentMonth), 
                day: currentDay
            }
            this.date = currentDate
            return currentDate
            
        }
    },                                                                                                                                                            
    created() {
        axios.get(
            'http://localhost:8000/api/v1/files/'
            ).then(
                response => this.forms = response.data
            ).catch(err => {console.log(err)});
    }
}
</script>

<style lang="less">

</style>