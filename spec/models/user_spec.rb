require 'rails_helper'

RSpec.describe User, :type => :model do
  # pending "add some examples to (or delete) #{__FILE__}"
  before do
  	@user = User.new(username: "Example User", password: "user@example.com")
  end
 subject { @user }
 it { should respond_to(:username) }
 it { should respond_to(:password) }
 it { should be_valid }

 describe "when name is not present" do
 	before { @user.username = ""}
 	it { should_not be_valid}
 end
 describe "when name is too long" do
	before { @user.username = "a" * 128 }
	it { should_not be_valid }
 end
 describe "when password is too long" do
    before { @user.password = "a" * 128 }
    it { should_not be_valid }
 end
 describe "signup page" do
    before { visit signup_path }
    it { should have_content('Sign up') }
    it { should have_title(full_title('Sign up')) }
 end

end
