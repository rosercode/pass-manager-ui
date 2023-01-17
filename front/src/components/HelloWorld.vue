<template>
  <div>
    <div class="module-header">
      <h3>passwd-ui</h3>
    </div>
    <div class="module-content">
      <div class="tool-bar">
        <el-input  placeholder="Title" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
        <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleSearch()">
          Search
        </el-button>
        <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleAdd">
          Add
        </el-button>
      </div>
      <el-table :data="tableData" border style="width: 100%" >
        <template v-for="column in bindTableColumns" >
          <el-table-column v-if="column.show"
                           :key="column.prop"
                           :prop="column.prop"
                           :label="column.label"
          ></el-table-column>
        </template>
        <el-table-column
          fixed="right"
          label="操作"
          width="200">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row)" type="text" size="small" >查看</el-button>
            <el-button @click="handleCopyPasswd(scope.row)" type="text" size="small">copy</el-button>
            <el-button @click="handleDelete(scope.row)" type="text" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <!-- 分页器 -->
      <div class="block" style="margin-top:15px;">
        <el-pagination align='center' @size-change="handleSizeChange" @current-change="handleCurrentChange"
                       :current-page="currentPage"
                       :page-sizes="[1,5,10,20]"
                       :page-size="pageSize"
                       layout="total, sizes, prev, pager, next, jumper"
                       :total="pageTotal">
        </el-pagination>
      </div>
      <!--  -->
      <el-drawer
        :title="drawerTitle"
        :visible.sync="drawer"
        :direction="direction"
        :before-close="handleClose">
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="简介">
            <el-input v-model="form.info"></el-input>
          </el-form-item>
          <el-form-item label="创建时间" disabled="true">
            <el-input v-model="form.create_time" disabled></el-input>
          </el-form-item>
          <el-form-item label="更新时间">
            <el-input v-model="form.update_time" disabled></el-input>
          </el-form-item>
          <el-form-item label="昵称">
            <el-input v-model="form.nickname"></el-input>
          </el-form-item>
          <el-form-item label="账号">
            <el-input v-model="form.account"></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input
              v-model="form.password"
              :type="type"
              class="pwd-input"
              placeholder="请输入密码"
            >
              <i
                slot="suffix"
                class="icon-style"
                :class="elIcon"
                autocomplete="auto"
                @click="flag = !flag"
              />
            </el-input>
          </el-form-item>
          <el-form-item label="网址">
            <el-input v-model="form.website"></el-input>
          </el-form-item>
          <el-form-item label="绑定的邮箱">
            <el-input v-model="form.bind_email"></el-input>
          </el-form-item>
          <el-form-item label="绑定手机号码">
            <el-input v-model="form.bind_phone"></el-input>
          </el-form-item>
          <el-form-item label="备注">
            <el-input v-model="form.comment"></el-input>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="onSubmit">Save</el-button>
            <el-button>Cancel</el-button>
          </el-form-item>
        </el-form>
      </el-drawer>
    </div>

  </div>
</template>

<script>
export default {
  computed: {
    type() {
      return this.flag ? "text" : "password";
    },
    elIcon() {
      return this.flag ? "el-icon-minus" : "el-icon-view";
    },
    bindTableColumns() {
      return this.tableColumns.filter((column) => column.show);
    }
  },
  created:function(){
    const _this = this
    this.$axios.get('/page', {
      params: {
        pageNum:1,
        pageSize: 5
      }
    }).then(function (response) {
      const res = response.data
      _this.tableData = res.data.data
      _this.pageSize = res.data.pageSize
      _this.currentPage = res.data.pageNum
      _this.pageTotal = res.data.pageTotal
      console.log(res)
    }).catch(function (error) {
      console.log(error);
    });
  },

  data() {
    return {
      confirm_new_pwd:"1",
      tableColumns:[
        {
          "prop":"id",
          "label": "id",
          "show": false
        },{
          "prop":"info",
          "label": "简介",
          "show": true
        },{
          "prop":"create_time",
          "label": "创建时间",
          "show": false
        },{
          "prop":"update_time",
          "label": "更新时间",
          "show": false
        },{
          "prop":"nickname",
          "label": "昵称",
          "show": false
        },{
          "prop":"account",
          "label": "账号",
          "show": true
        },{
          "prop":"password",
          "label": "密码",
          "show": false
        },{
          "prop":"website",
          "label": "网址",
          "show": true
        },{
          "prop":"bind_email",
          "label": "绑定邮箱",
          "show": false
        },{
          "prop":"bind_phone",
          "label": "绑定手机号码",
          "show": false
        },{
          "prop":"comment",
          "label": "注释",
          "show": true
        }
      ],
      tableData: [],
      currentPage:1,
      pageSize:10,
      pageTotal:20,

      drawerTitle:"",
      drawer: false,
      direction: 'rtl',

      form: {
        info: '',
        create_time:'',
        update_time:'',
        nickname: '',
        account: '',
        password: '',
        website: '',
        bind_email: '',
        bind_phone: '',
        comment: ''
      },

      pwd: "123456",
      flag: false
    }
  },
  methods:{
    pageSelect(){
      const _this = this
      this.$axios.get('/page', {
        params: {
          pageNum:this.currentPage,
          pageSize:this.pageSize
        }
      }).then(function (response) {
        const res = response.data
        _this.tableData = res.data.data
        _this.pageSize = res.data.pageSize
        _this.currentPage = res.data.pageNum
        _this.pageTotal = res.data.pageTotal
        console.log(res)
      }).catch(function (error) {
        console.log(error);
      });
    },

    // copy password to clipboard
    handleCopyPasswd(row){
      console.log(row)
      let transfer = document.createElement('input');
      document.body.appendChild(transfer);
      transfer.value = row.password;  // 这里表示想要复制的内容
      transfer.focus();
      transfer.select();
      if (document.execCommand('copy')) {
        document.execCommand('copy');
      }
      transfer.blur();
      const h = this.$createElement;
      this.$notify({
        title: '提示',
        message: h('i', { style: 'color: teal'}, '复制成功')
      });
      console.log('复制成功');

      document.body.removeChild(transfer);
    },

    handleClick(row){
      console.log(row)
      this.drawer = true
      this.form = row
      this.drawerTitle = "编辑"

    },
    //每页条数改变时触发 选择一页显示多少行
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      this.pageSize = val;
      this.pageSelect()
    },
    //当前页改变时触发 跳转其他页
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.currentPage = val;
      this.pageSelect()
    },
    handleClose(done) {
      done();
    },
    // 搜索表格内容 请求后端
    handleSearch(){

    },
    handleAdd(){
      this.form = {}
      this.drawer = true
      this.drawerTitle = "添加"
    },
    handleDelete(row){
      const _this = this
      const id = row['id']
      this.$confirm('此操作将删除这条记录, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        //点击确定的操作(调用接口)
        _this.$axios.get('/delete', {
          params: {
            id:id
          }
        }).then(function (response) {
          _this.pageSelect()
          console.log(res)
        }).catch(function (error) {
          console.log(error);
        });
      }).catch(() => {
        //几点取消的提示
        const h = _this.$createElement;
        _this.$notify({
          title: '提示',
          message: h('i', { style: 'color: teal'}, '取消操作')
        });
      });

    },
    // 保存，或者 更新数据
    onSubmit() {
      console.log('submit!');
      // this.form['create_time'] = this.form['create_time1'] + this.form['create_time2']
      // this.form['update_time'] = this.form['update_time1'] + this.form['update_time2']
      var url = this.form['id'] === undefined || this.form['id'] === '' ? '/add' : '/update'
      const _this = this
      this.$axios.get(url, {
        params: _this.form
      }).then(function (response) {
        const h = _this.$createElement;
        _this.$notify({
          title: '提示',
          message: h('i', { style: 'color: teal'}, '操作完成')
        });
        _this.drawer = false
        _this.pageSelect()
        console.log(response)
      }).catch(function (error) {
        console.log(error);
      });
    }
  }
}
</script>

<style>

.el-table .hidden-row {
  display: none;
}
.tool-bar{
  text-align: right;
}
</style>
