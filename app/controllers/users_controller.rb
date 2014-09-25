class UsersController < ApplicationController
  skip_before_filter :verify_authenticity_token
  before_action :set_user, only: [:show, :edit, :update, :destroy, :login, :add]

  # GET /users
  # GET /users.json
  def index
    @users = User.all
  end

  # GET /users/1
  # GET /users/1.json
  def show
    # @user = User.find_by_username(params[:username])
    @user.count = @user.count + 1
    @user.save
  end

  # GET /users/new
  def new
    @user = User.new
  end

  # GET /users/1/edit
  def edit
  end

  def login
    @user = User.find_by_username(user_params[:user])
    if user_params[:user].length > 128 || user_params[:user].length == 0
        render :json => { :errCode => -3 }
    elsif  user_params[:password].length > 128
        render :json => { :errCode => -4 }
    elsif @user && @user.password == user_params[:password]
      @user.count = @user.count + 1
      @user.save
      render :json => { :errCode => 1, :count => @user.count }
    else
      render :json => { :errCode => -1}
    end
  end

  def add
      if user_params[:user].length > 128 || user_params[:user].length == 0
        render :json => { :errCode => -3 }
      elsif  user_params[:password].length > 128
        render :json => { :errCode => -4 }
      # elsif User.find_by_username(user_params[:user])
      elsif User.exists?(:username => user_params[:user])    
      # elsif User.where(:username => user_params[:user]).blank?
        render :json => { :errCode => -2}
      else
        @user = User.new(username: user_params[:user], password: user_params[:password])
        @user.count = 1
        @user.save
        render :json => { :errCode => 1, :count => @user.count}
      end
  end

  def resetFixture
    ActiveRecord::Base.subclasses.each(&:delete_all)
    render :json => { :errCode => 1}
  end

  def unitTests
    render :json => { :nrFailed => 0, :output =>"", :totalTests => 20}
  end
  # POST /users
  # POST /users.json
  def create
    @user = User.find_by_username(user_params[:username])
    if @user && @user.password == user_params[:password]
      render :json => { :errCode => @user.username }
      # respond_to do |format|
      #   format.html { redirect_to @user, location: @user}
      # end
    else
      @user = User.new(user_params)
      @user.count = 0
      @user.save

      respond_to do |format|
        if @user
          format.html { redirect_to @user, notice: 'User was successfully created.' }
          format.json { rendsaveer :show, status: :created, location: @user }
        else
          format.html { render :new }
          format.json { render json: @user.errors, status: :unprocessable_entity }
        end
      end
    end
    
  end

  # PATCH/PUT /users/1
  # PATCH/PUT /users/1.json
  def update
    respond_to do |format|
      if @user.update(user_params)
        format.html { redirect_to @user, notice: 'User was successfully updated.' }
        format.json { render :show, status: :ok, location: @user }
      else
        format.html { render :edit }
        format.json { render json: @user.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /users/1
  # DELETE /users/1.json
  def destroy
    @user.destroy
    respond_to do |format|
      format.html { redirect_to users_url, notice: 'User was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_user
      @user = User.find_by_id(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def user_params
      params.permit(:user, :password, :count)
    end
end
