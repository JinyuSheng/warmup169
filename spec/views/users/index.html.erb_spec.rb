require 'rails_helper'

RSpec.describe "users/index", :type => :view do
  before(:each) do
    assign(:users, [
      User.create!(
        :username => "Username",
        :password => "Password",
        :count => 1
      ),
      User.create!(
        :username => "Username",
        :password => "Password",
        :count => 1
      )
    ])
  end

  # it "renders a list of users" do
  #   render
  #   assert_select "tr>td", :text => "Username".to_s, :count => 2
  #   assert_select "tr>td", :text => "Password".to_s, :count => 2
  #   assert_select "tr>td", :text => 1.to_s, :count => 2
  # end
end
