require 'rails_helper'

RSpec.describe "users/new", :type => :view do
  before(:each) do
    assign(:user, User.new(
      :username => "MyString",
      :password => "MyString",
      :count => 1
    ))
  end

  # it "renders new user form" do
  #   render

  #   assert_select "form[action=?][method=?]", users_path, "post" do

  #     assert_select "input#user_username[name=?]", "user[username]"

  #     assert_select "input#user_password[name=?]", "user[password]"

  #     assert_select "input#user_count[name=?]", "user[count]"
  #   end
  # end
end
