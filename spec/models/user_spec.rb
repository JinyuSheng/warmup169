require 'rails_helper'

RSpec.describe User, :type => :model do
  # pending "add some examples to (or delete) #{__FILE__}"
  before do
  	@user = User.new(username: "ExampleUser", password: "thisisapassword")
  end
  # makes @user the default subject of the test example
 subject { @user }
 it { should respond_to(:username) }
 it { should respond_to(:password) }
 it { should be_valid }

 describe "when name is not present" do
 	before { @user.username = ""}
 	it { should_not be_valid}
 end
 describe "when name is too long" do
	before { @user.username = "a" * 129 }
	it { should_not be_valid }
 end
 describe "when password is too long" do
    before { @user.password = "a" * 129 }
    it { should_not be_valid }
 end
 describe "when username is already present" do
 	before do
	    user_with_same_username = @user.dup
	    user_with_same_username.save
    end
    it {should_not be_valid}
 end
 describe "when name has blank spaces" do
 	before { @user.username = "    "}
 	it { should_not be_valid}
 end
 describe "when password is not present, should be fine" do
 	before { @user.password = ""}
 	it { should be_valid}
 end
end