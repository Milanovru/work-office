<template>
    <section>
        <select name="documents" :selected="true" v-model="selected">
            <option v-for="option in options" :key="option">{{option}}</option>
        </select>
        <div class="html-form" v-html="chek_form"></div>
    </section>
</template>

<script>
import { useMainStore } from "../stores/mainStore";
import { mapState } from 'pinia'
import axios from 'axios'


export default {
    data() {
        return {
            selected: 'form1.docx',
            options: '',
            html_form: null
        }
    },
    methods: {
        get_documents_list() {
            axios.get(
            'http://localhost:8000/api/v1/files/'
            ).then(response => {
                this.options = response.data
            }).catch(err => {
                console.log(err);
            })
        }, 
    },
    computed: {
        ...mapState(useMainStore, ['renderHtml']),
        chek_form () {
            axios.get(
            `http://localhost:8000/api/v1/files/${this.selected}`
            ).then(
                response => this.html_form = response.data
            ).catch(error => console.error(error));
            return this.html_form
        }
    },
    created() {
        this.get_documents_list()
    }
}
</script>

<style lang='less'>

.html-form {
    width: 850px;

    table:nth-child(2) {
        width: 100%;
      td { 
          display: block;
          margin-left: 45%;          
      }
    }

    table:nth-child(4),
    table:nth-child(7) {
        width: 100%;

        td:last-child {
            text-align: right;
        }
    }

    table:nth-child(1),
    table:nth-child(5) {
        tr {
            text-align: center;
            td:nth-child(1) {
                display: block;
                margin-left: 20px;
            }
            td:nth-child(3) {
                display: block;
                margin-left: 280px;
            }
        }
    }

    table:nth-child(6) {
        width: 100%;
        td { 
            display: block;
            margin-left: 15%;
        }
    }

    p:nth-child(3) {
        text-indent: 20px;
        text-align: justify;

    }

.input-rank,
.input-name,
.input-position {
    width: 120px;
}

}


</style>
