var LoginForm = React.createClass({
  getInitialState: function() {
    var uname = $.cookie('username');
    var passwd = $.cookie('password');
    return {username: uname, password: passwd};
  },
  handleUsernameChange: function(e) {
    this.setState({username: e.target.value});
  },
  handlePasswordChange: function(e) {
    this.setState({password: e.target.value});
  },
  handleLoginAction: function(e) {
    var data = {
      'username': this.state.username,
      'password': this.state.password
    };
    $.ajax({
      url: login_url,
      dataType: 'json',
      type: 'POST',
      data: data,
      success: function(data) {
        if (data.success == 'false') {
          alert('Username or Password incorrect');
        } else {
          $.removeCookie('username', { path: '/' });
          $.removeCookie('password', { path: '/' });
          $.cookie('username', this.state.username, {path: '/' });
          $.cookie('password', this.state.password, {path: '/' });
          document.location.href = 'static/uploader.html';
        }
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
        alert('服务器错误');
      }.bind(this)
    });
  },
  render: function() {
    return (
      <div className="col-md-4 col-md-offset-4 login-form">
      <p className="title">雪球用户登录</p>

      <div className="form-group username-group">
      <label className="control-label" id="account-label">用户名:</label>
      <input type="text" className="form-control" id="inputAccount" placeholder="请输入雪球用户名(必须为邮箱)" onChange={this.handleUsernameChange} value={this.state.username}/>
      </div>

      <div className="form-group password-group">
      <label className="control-label" id="password-label">密码:</label>
      <input type="password" className="form-control" id="inputPassword" placeholder="请输入密码" onChange={this.handlePasswordChange} value={this.state.password}/>
      </div>

      <button className="btn btn-primary" id="login-btn" onClick={this.handleLoginAction}>登录</button>
      </div>
    );
  }
});
ReactDOM.render(
  <LoginForm />,
  document.getElementById('content')
);
